from PySide6.QtWidgets import QMessageBox

from infra.entities.paciente import Paciente
from infra.repository.paciente_repository import PacienteRepository
from infra.repository.consulta_repository import ConsultaRepository
from infra.repository.medico_repository import MedicoRepository
from services.main_window_service import MainWindowService

class PacienteService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.consulta_repository = ConsultaRepository()
        self.medico_repository = MedicoRepository()
        self.paciente_repository = PacienteRepository()

    def insert_paciente(self, main_window):
        cpf_paciente = main_window.txt_cpf.text()
        paciente = Paciente()
        paciente.nome = main_window.txt_nome.text()
        paciente.numero_seguro = main_window.txt_numero_seguro.text()
        paciente.historico_medico = main_window.txt_historico_medico.text()
        paciente.idade = main_window.txt_idade.text()
        paciente.telefone_contato = main_window.txt_telefone.text()
        paciente.cpf = main_window.txt_cpf.text()
        paciente.email = main_window.txt_email.text()
        paciente.nome_emergencia = main_window.txt_nome_contanto_emergencia.text()
        paciente.telefone_emergencia = main_window.txt_contato_emergencia.text()
        paciente.ativo = True

        if not paciente.campos_obrigatorios_preenchidos():
            QMessageBox.warning(main_window, 'Pacientes', 'Todos os campos obrigatórios devem ser preenchidos!')
            return

        try:
            cpf_existe = self.paciente_repository.select_paciente_by_cpf(cpf_paciente)
            if cpf_existe:
                QMessageBox.information(main_window, 'Pacientes', 'CPF já está cadastrado no sistema!')
                return

            email_existe = self.paciente_repository.select_paciente_by_email(paciente.email)
            if email_existe:
                QMessageBox.information(main_window, 'Pacientes', 'E-mail já está cadastrado no sistema!')
                return

            numero_seguro_existe = self.paciente_repository.select_paciente_by_numero_seguro(paciente.numero_seguro)
            if numero_seguro_existe:
                QMessageBox.information(main_window, 'Pacientes', 'Número de seguro já está cadastrado no sistema!')
                return

            self.paciente_repository.insert_one_paciente(paciente)
            main_window.txt_nome.clear()
            main_window.txt_numero_seguro.clear()
            main_window.txt_historico_medico.clear()
            main_window.txt_idade.clear()
            main_window.txt_telefone.clear()
            main_window.txt_cpf.clear()
            main_window.txt_email.clear()
            main_window.txt_nome_contanto_emergencia.clear()
            main_window.txt_contato_emergencia.clear()
            QMessageBox.information(main_window, 'Pacientes', 'Paciente cadastrado com sucesso!')

        except Exception as e:
            QMessageBox.warning(main_window, 'Pacientes', f'Erro ao cadastrar Paciente\n'
                                                          f'Erro : {e}')

    def update_paciente(self, main_window):
        cpf_paciente = main_window.txt_cpf.text()
        if cpf_paciente != '':
            try:
                paciente_update = self.paciente_repository.select_paciente_by_cpf(cpf_paciente)
                paciente_update.nome = main_window.txt_nome.text()
                paciente_update.cpf = main_window.txt_cpf.text()
                paciente_update.idade = main_window.txt_idade.text()
                paciente_update.email = main_window.txt_email.text()
                paciente_update.nome_emergencia = main_window.txt_nome_contanto_emergencia.text()
                paciente_update.telefone_emergencia = main_window.txt_contato_emergencia.text()
                paciente_update.numero_seguro = main_window.txt_numero_seguro.text()
                paciente_update.historico_medico = main_window.txt_historico_medico.text()
                paciente_update.telefone_contato = main_window.txt_telefone.text()

                self.paciente_repository.update_paciente(paciente_update)
                QMessageBox.information(main_window, "Cadastro de paciente", "Paciente atualizado com sucesso!")

                main_window.txt_nome.clear()
                main_window.txt_numero_seguro.clear()
                main_window.txt_historico_medico.clear()
                main_window.txt_idade.clear()
                main_window.txt_telefone.clear()
                main_window.txt_cpf.clear()
                main_window.txt_email.clear()
                main_window.txt_nome_contanto_emergencia.clear()
                main_window.txt_contato_emergencia.clear()
                main_window.btn_editar.setEnabled(False)
                main_window.txt_cpf.setReadOnly(False)
            except Exception as e:
                QMessageBox.warning(main_window, "Pacientes", f'Problema ao atualizar paciente. \n'
                                                              f'Erro: {e}')

    def select_paciente_consulta(self, main_window):
        cpf_paciente = main_window.txt_cpf.text()
        if cpf_paciente == '':
            QMessageBox.information(main_window, 'Pacientes', 'Por favor, informe o CPF e clique em Consultar')
            return
        else:
            paciente_consulta = self.paciente_repository.select_paciente_by_cpf(cpf_paciente)
            try:
                if not paciente_consulta:
                    QMessageBox.information(main_window, 'Pacientes', 'O CPF informado não está cadastrado no sistema!')
                    return
                else:
                    main_window.btn_editar.setEnabled(True)
                    main_window.txt_nome.setText(paciente_consulta.nome)
                    main_window.txt_numero_seguro.setText(paciente_consulta.numero_seguro)
                    main_window.txt_historico_medico.setText(paciente_consulta.historico_medico)
                    main_window.txt_idade.setText(str(paciente_consulta.idade))
                    main_window.txt_telefone.setText(paciente_consulta.telefone_contato)
                    main_window.txt_cpf.setText(paciente_consulta.cpf)
                    main_window.txt_email.setText(paciente_consulta.email)
                    main_window.txt_nome_contanto_emergencia.setText(paciente_consulta.nome_emergencia)
                    main_window.txt_contato_emergencia.setText(paciente_consulta.telefone_emergencia)
                    main_window.txt_cpf.setReadOnly(True)
            except Exception as e:
                QMessageBox.warning(main_window, 'Pacientes', f'Erro ao Consultar Paciente\n'
                                                              f'Erro : {e}')