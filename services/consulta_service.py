from datetime import datetime, time
from PySide6.QtWidgets import QMessageBox
import time

from infra.repository.consulta_repository import ConsultaRepository
from infra.repository.paciente_repository import PacienteRepository
from infra.repository.medico_repository import MedicoRepository
from services.main_window_service import MainWindowService

from services.email_service import ServicoEmail
from infra.config.config_email import ConfiguracaoEmail

class ConsultaService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.consulta_repository = ConsultaRepository()
        self.medico_repository = MedicoRepository()
        self.paciente_repository = PacienteRepository()

        self.servico_email = ServicoEmail(ConfiguracaoEmail())

    def insert_consulta(self, main_window):

        if main_window.txt_cpf_paciente.text() == '':
            QMessageBox.information(main_window, 'Agendar Consulta', 'Por favor, informe um paciente!')
            return

        elif main_window.cb_hora.currentText() == 'Selecione um horário' \
                or main_window.cb_medico_2.currentText() == 'Selecione um profissional' \
                or main_window.cb_exame.currentText() == 'Selecione um tipo de consulta' \
                or main_window.txt_agendar_data.text() == '':
            QMessageBox.information(main_window, 'Agendar Consulta', 'Todos os campos são obrigatórios!')
            return

        else:
            if main_window.txt_agendar_data.text() != '':
                data_atual = datetime.now()
                data_inserida = datetime.strptime(main_window.txt_agendar_data.text(), '%d/%m/%Y')
                hora_inserida = datetime.strptime(main_window.cb_hora.currentText(), '%H:%M')
                data_hora_inserida = datetime.combine(data_inserida.date(), hora_inserida.time())
                if data_hora_inserida < data_atual:
                    QMessageBox.information(main_window, 'Agendar Consulta', 'Por favor, selecione uma data e hora futuras.')
                    return

                paciente = self.paciente_repository.select_paciente_by_cpf(main_window.txt_cpf_paciente.text())
                data = main_window.txt_agendar_data.text()
                hora = main_window.cb_hora.currentText()
                medico = self.medico_repository.select_medico_by_name(main_window.cb_medico_2.currentText())
                exame = main_window.cb_exame.currentText()
                informacoes_adicionais = main_window.txt_informacoes_adicionais.toPlainText()
                consulta_protocolo = "AG" + str(int(time.time()))
                try:
                    self.consulta_repository.insert_consulta(consulta_protocolo, paciente, medico, data, hora, exame, informacoes_adicionais)
                    self.limpar_agendamento_consulta(main_window)
                    self.servico_email.enviar_email_paciente(paciente.nome, paciente.email, medico.nome, consulta_protocolo, data, hora)

                    QMessageBox.information(main_window, 'Agendar Consulta', 'Consulta cadastrada com sucesso')
                except Exception as e:
                    QMessageBox.warning(main_window, 'Agendar Consulta', f'Erro ao cadastrar consulta.\n'
                                                                          f'Erro : {e}')

    def update_consulta_reagendar(self, main_window):
        protocolo = main_window.lineEdit_2.text()
        motivo = main_window.cb_cancelamento.currentText()
        consulta = self.consulta_repository.select_consultas_protolo(protocolo)
        if consulta:
            if motivo == 'Selecione o motivo':
                QMessageBox.information(main_window, 'Agendar Consulta',
                                        'Informe o motivo do reagendamento!')
                return
            data = main_window.txt_agendar_data.text()
            hora = main_window.cb_hora.currentText()
            data_inserida = datetime.strptime(main_window.txt_agendar_data.text(), '%d/%m/%Y')
            hora_inserida = datetime.strptime(main_window.cb_hora.currentText(), '%H:%M')
            data_hora_inserida = datetime.combine(data_inserida.date(), hora_inserida.time())
            consulta.data_consulta = data_hora_inserida
            consulta.medico.nome = main_window.cb_medico_2.currentText()
            consulta.tipo_exame = main_window.cb_exame.currentText()
            consulta.motivo = motivo
            self.consulta_repository.update_consulta(consulta)
            QMessageBox.information(main_window, 'Agendar consulta', 'Consulta reagendada com sucesso!')
            self.limpar_agendamento_consulta(main_window)
            self.service_main_window.populate_consultas_ativas(main_window)
            self.servico_email.enviar_email_paciente_reagendamento(consulta.paciente.nome, consulta.paciente.email,
                                                     consulta.medico.nome, consulta.consulta_protocolo,
                                                     data, hora)
        else:
            QMessageBox.information(main_window, 'Agendar consulta', 'Erro ao reagendar consulta! \n'
                                                                     'Verifique os dados informados.')
            print("Consulta não encontrada.")

    def update_consulta_cancelar(self, main_window):
        protocolo = main_window.lineEdit_2.text()
        motivo = main_window.cb_cancelamento.currentText()
        consulta = self.consulta_repository.select_consultas_protolo(protocolo)
        if consulta:
            if motivo == 'Selecione o motivo':
                QMessageBox.information(main_window, 'Agendar Consulta',
                                        'Informe o motivo do cancelamento!')
                return
            consulta.status = False
            consulta.motivo = motivo
            self.consulta_repository.update_consulta(consulta)
            QMessageBox.information(main_window, 'Agendar consulta', 'Consulta cancelada com sucesso!')
            self.limpar_agendamento_consulta(main_window)
            self.service_main_window.populate_consultas_ativas(main_window)
        else:
            QMessageBox.information(main_window, 'Agendar consulta', 'Erro ao cancelar consulta! \n'
                                                                     'Verifique os dados informados.')
            print("Consulta não encontrada.")

    def select_paciente_agenda(self, main_window):
        cpf_paciente = main_window.txt_cpf_paciente.text()
        if cpf_paciente == '':
            QMessageBox.information(main_window, 'Agendar consulta', 'Por favor, informe o CPF e clique em Consultar Paciente')
            return
        else:
            paciente_consulta = self.paciente_repository.select_paciente_by_cpf(cpf_paciente)
            try:
                if not paciente_consulta:
                    QMessageBox.information(main_window, 'Agendar consulta', 'O CPF informado não está cadastrado no sistema!')
                    return
                else:
                    main_window.txt_nome_paciente.setText(paciente_consulta.nome)

            except Exception as e:
                QMessageBox.warning(main_window, 'Agendar consulta', f'Erro ao Consultar Paciente\n'
                                                                     f'Erro : {e}')

    def select_consultas_agendadas(self, main_window):
        nome_medico = main_window.cb_medico.currentText()
        data = main_window.lineEdit.text()

        if len(data) == 10 and data != '//':
            consultas_ativas = self.consulta_repository.select_consultas_ativas_por_data(data)
            if consultas_ativas:
                self.service_main_window.populate_consultas_ativas_medico(main_window, consultas_ativas)
            else:
                QMessageBox.information(main_window, 'Consultas agendadas',
                                        'Nenhuma consulta encontrada nessa data!')
                self.service_main_window.populate_consultas_ativas(main_window)
                return

        if nome_medico != 'Selecione um médico':
            medico = self.medico_repository.select_medico_by_name(nome_medico)
            main_window.tb_consulta_agendada.setRowCount(0)
            consultas_ativas_medico = self.consulta_repository.select_consultas_ativas_por_medico_e_data(medico.id, data)
            if consultas_ativas_medico:
                self.service_main_window.populate_consultas_ativas_medico(main_window, consultas_ativas_medico)
            else:
                QMessageBox.information(main_window, 'Consultas agendadas',
                                        'Nenhuma consulta encontrada para esse médico e data!')
                self.service_main_window.populate_consultas_ativas(main_window)
                return

        if nome_medico == 'Selecione um médico' and data == '//':
            QMessageBox.information(main_window, 'Consultas agendadas', 'Selecione um médico e/ou uma data!')
            self.service_main_window.populate_consultas_ativas(main_window)
            return

    def select_consulta_por_protocolo(self, main_window):
        protocolo_consulta = main_window.lineEdit_2.text()
        if protocolo_consulta == '':
            QMessageBox.information(main_window, 'Gerenciar consulta', 'Por favor, informe o protoco que deseja consultar!')
            return
        else:
            consulta = self.consulta_repository.select_consultas_protolo(protocolo_consulta)
            try:
                if not consulta:
                    QMessageBox.information(main_window, 'Gerenciar consulta', 'O Protocolo informado não está cadastrado no sistema!')
                    return
                else:
                    data = consulta.data_consulta.strftime('%d/%m/%Y')
                    hora = consulta.data_consulta.strftime('%H:%M')
                    main_window.txt_nome_paciente.setText(consulta.paciente.nome)
                    main_window.txt_agendar_data.setText(str(data))
                    main_window.cb_hora.setCurrentText(str(hora))
                    main_window.cb_medico_2.setCurrentText(consulta.medico.nome)
                    main_window.cb_exame.setCurrentText(consulta.tipo_exame)
                    main_window.cb_cancelamento.setEnabled(True)
                    main_window.btn_reagendar.setEnabled(True)
                    main_window.btn_cancelar_consulta.setEnabled(True)
                    main_window.btn_confirmar.setEnabled(False)
                    main_window.btn_consultar_paciente.setEnabled(False)

            except Exception as e:
                QMessageBox.warning(main_window, 'Gerenciar consulta', f'Erro ao buscar consulta\n'
                                                                     f'Erro : {e}')
                print(e)

    def select_consultas_dia(self, main_window):
        self.nome_medico = main_window.cb_medico.currentText()
        main_window.lineEdit.clear()
        if self.nome_medico != 'Selecione um médico':
            data_atual = datetime.now()
            data = datetime.strftime(data_atual, '%d/%m/%Y')
            try:
                medico = self.medico_repository.select_medico_by_name(self.nome_medico)
                consultas_ativas_medico = self.consulta_repository.select_consultas_ativas_por_medico_e_data(medico.id, data)
                if consultas_ativas_medico:
                    self.service_main_window.populate_consultas_ativas_medico(main_window, consultas_ativas_medico)
                else:
                    QMessageBox.information(main_window, 'Consultas agendadas',
                                            'Nenhuma consulta encontrada para esse médico!')
                    self.service_main_window.populate_consultas_ativas(main_window)

            except Exception as e:
                print(f'Erro : {e}')
        else:
            try:
                consultas_ativas_medico = self.consulta_repository.select_consultas_ativas_por_dia()
                if consultas_ativas_medico:
                    self.service_main_window.populate_consultas_ativas_medico(main_window, consultas_ativas_medico)
                else:
                    QMessageBox.information(main_window, 'Consultas agendadas',
                                            'Nenhuma consulta encontrada para esse dia!')
                    self.service_main_window.populate_consultas_ativas(main_window)

            except Exception as e:
                print(f'Erro : {e}')

    def select_consultas_semana(self, main_window):
        self.nome_medico = main_window.cb_medico.currentText()
        main_window.lineEdit.clear()
        if self.nome_medico != 'Selecione um médico':
            try:
                medico = self.medico_repository.select_medico_by_name(self.nome_medico)
                consultas_ativas_medico = self.consulta_repository.select_consultas_para_semana_atual_medico(medico.id)
                if consultas_ativas_medico:
                    self.service_main_window.populate_consultas_ativas_medico(main_window, consultas_ativas_medico)
                else:
                    QMessageBox.information(main_window, 'Consultas agendadas',
                                            'Nenhuma consulta encontrada para esse médico!')
                    self.service_main_window.populate_consultas_ativas(main_window)
            except Exception as e:
                print(f'Erro : {e}')
        else:
            try:
                consultas_ativas_medico = self.consulta_repository.select_consultas_para_semana_atual()
                if consultas_ativas_medico:
                    self.service_main_window.populate_consultas_ativas_medico(main_window, consultas_ativas_medico)
                else:
                    QMessageBox.information(main_window, 'Consultas agendadas',
                                            'Nenhuma consulta encontrada para essa semana!')
                    self.service_main_window.populate_consultas_ativas(main_window)
            except Exception as e:
                print(f'Erro : {e}')

    def select_consultas_mes(self, main_window):
        self.nome_medico = main_window.cb_medico.currentText()
        main_window.lineEdit.clear()
        if self.nome_medico != 'Selecione um médico':
            try:
                medico = self.medico_repository.select_medico_by_name(self.nome_medico)
                consultas_ativas_medico = self.consulta_repository.select_consultas_para_mes_atual_medico(medico.id)
                if consultas_ativas_medico:
                    self.service_main_window.populate_consultas_ativas_medico(main_window, consultas_ativas_medico)
                else:
                    QMessageBox.information(main_window, 'Consultas agendadas',
                                            'Nenhuma consulta encontrada para esse médico!')
                    self.service_main_window.populate_consultas_ativas(main_window)
            except Exception as e:
                print(f'Erro : {e}')
        else:
            try:
                consultas_ativas_medico = self.consulta_repository.select_consultas_para_mes_atual()
                if consultas_ativas_medico:
                    self.service_main_window.populate_consultas_ativas_medico(main_window, consultas_ativas_medico)
                else:
                    QMessageBox.information(main_window, 'Consultas agendadas',
                                            'Nenhuma consulta encontrada para esse mês!')
                    self.service_main_window.populate_consultas_ativas(main_window)
            except Exception as e:
                print(f'Erro : {e}')

    def limpar_agendamento_consulta(self, main_window):
        main_window.txt_cpf_paciente.clear()
        main_window.txt_nome_paciente.clear()
        main_window.txt_agendar_data.clear()
        main_window.cb_hora.setCurrentIndex(0)
        main_window.cb_medico_2.setCurrentIndex(0)
        main_window.cb_exame.setCurrentIndex(0)
        main_window.txt_informacoes_adicionais.clear()
        main_window.lineEdit_2.clear()
        main_window.cb_cancelamento.setCurrentIndex(0)
        main_window.btn_confirmar.setEnabled(True)
        main_window.btn_consultar_paciente.setEnabled(True)
        main_window.cb_cancelamento.setEnabled(False)
        main_window.btn_reagendar.setEnabled(False)
        main_window.btn_cancelar_consulta.setEnabled(False)
