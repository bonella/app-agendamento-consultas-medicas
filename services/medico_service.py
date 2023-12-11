from PySide6.QtWidgets import QMessageBox

from infra.entities.medico import Medico
from infra.repository.medico_repository import MedicoRepository

class MedicoService:
    def __init__(self):

         self.medico_repository = MedicoRepository()

    def insert_medico(self, main_window):
        numero_crm = main_window.txt_numero_crm.text()
        email_medico = main_window.txt_email_medico.text()
        medico = Medico()
        medico.nome = main_window.txt_nome_medico.text()
        medico.especialidade = main_window.txt_especialidade_medico.text()
        medico.telefone_contato = main_window.txt_telefone_medico.text()
        medico.email = main_window.txt_email_medico.text()
        medico.numero_crm = main_window.txt_numero_crm.text()
        medico.idade = main_window.txt_idade_medico.text()
        medico.ativo = True

        if not medico.campos_obrigatorios_preenchidos():
            QMessageBox.warning(main_window, 'Medicos', 'Todos os campos obrigatórios devem ser preenchidos!')
            return

        try:
            crm_existe = self.medico_repository.select_medico_by_crm(numero_crm)
            if crm_existe:
                QMessageBox.information(main_window, 'Medicos', 'CRM já está cadastrado no sistema!')
                return

            email_existe = self.medico_repository.select_medico_by_email(email_medico)
            if email_existe:
                QMessageBox.information(main_window, 'Medicos', 'E-mail já está cadastrado no sistema!')
                return

            self.medico_repository.insert_one_medico(medico)
            main_window.txt_nome_medico.clear()
            main_window.txt_especialidade_medico.clear()
            main_window.txt_telefone_medico.clear()
            main_window.txt_email_medico.clear()
            main_window.txt_numero_crm.clear()
            main_window.txt_idade_medico.clear()
            QMessageBox.information(main_window, 'Medicos', 'Medico cadastrado com sucesso!')

        except Exception as e:
            QMessageBox.warning(main_window, 'Medicos', f'Erro ao cadastrar Medico\n'
                                                          f'Erro : {e}')

    def update_medico(self, main_window):
        crm_medico = main_window.txt_numero_crm.text()
        if crm_medico != '':
            try:
                medico_update = self.medico_repository.select_medico_by_crm(crm_medico)
                medico_update.nome = main_window.txt_nome_medico.text()
                medico_update.especialidade = main_window.txt_especialidade_medico.text()
                medico_update.telefone_contato = main_window.txt_telefone_medico.text()
                medico_update.email = main_window.txt_email_medico.text()
                medico_update.numero_crm = main_window.txt_numero_crm.text()
                medico_update.idade = main_window.txt_idade_medico.text()

                self.medico_repository.update_medico(medico_update)
                QMessageBox.information(main_window, "Medicos", "Medico atualizado com sucesso!")

                main_window.txt_nome_medico.clear()
                main_window.txt_especialidade_medico.clear()
                main_window.txt_telefone_medico.clear()
                main_window.txt_email_medico.clear()
                main_window.txt_numero_crm.clear()
                main_window.txt_idade_medico.clear()
                main_window.btn_editar_medico.setEnabled(False)
            except Exception as e:
                QMessageBox.warning(main_window, "Medicos", f'Problema ao atualizar médico. \n'
                                                            f'Erro: {e}')

    def select_medico_consulta(self, main_window):
        crm_medico = main_window.txt_numero_crm.text()
        if crm_medico == '':
            QMessageBox.information(main_window, 'Medicos', 'Por favor, informe o CRM e clique em Consultar')
            return
        else:
            medico_consulta = self.medico_repository.select_medico_by_crm(crm_medico)
            try:
                if not medico_consulta:
                    QMessageBox.information(main_window, 'Medicos', 'O CRM informado não está cadastrado no sistema!')
                    return
                else:
                    main_window.btn_editar_medico.setEnabled(True)
                    main_window.txt_nome_medico.setText(medico_consulta.nome)
                    main_window.txt_especialidade_medico.setText(medico_consulta.especialidade)
                    main_window.txt_telefone_medico.setText(medico_consulta.telefone_contato)
                    main_window.txt_email_medico.setText(medico_consulta.email)
                    main_window.txt_numero_crm.setText(medico_consulta.numero_crm)
                    main_window.txt_idade_medico.setText(str(medico_consulta.idade))

            except Exception as e:
                QMessageBox.warning(main_window, 'Medicos', f'Erro ao Consultar Medico\n'
                                                                       f'Erro : {e}')