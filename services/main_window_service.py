from PySide6.QtWidgets import QTableWidgetItem

from infra.repository.consulta_repository import ConsultaRepository
from infra.repository.medico_repository import MedicoRepository
from infra.repository.paciente_repository import PacienteRepository

class MainWindowService:
    def __init__(self):
        self.consulta_repository = ConsultaRepository()
        self.paciente_repository = PacienteRepository()
        self.medico_repository = MedicoRepository()

    def populate_combo_medicos(self, main_window):
        main_window.medicos = self.medico_repository.select_all_medicos()
        for medico in main_window.medicos[:]:
            if not medico.ativo:
                main_window.medicos.remove(medico)
        for medico in main_window.medicos:
            main_window.cb_medico_2.addItem(medico.nome)

    def populate_combo_medicos_agendamento(self, main_window):
        main_window.medicos = self.medico_repository.select_all_medicos()
        for medico in main_window.medicos[:]:
            if not medico.ativo:
                main_window.medicos.remove(medico)
        for medico in main_window.medicos:
            main_window.cb_medico.addItem(medico.nome)

    def populate_consultas_ativas(self, main_window):
        main_window.tb_consulta_agendada.setRowCount(0)
        consultas_ativas = self.consulta_repository.select_consultas_ativas()
        main_window.tb_consulta_agendada.setRowCount(len(consultas_ativas))
        linha = 0
        for consulta in consultas_ativas:
            coluna = 0
            for valor in consulta:
                main_window.tb_consulta_agendada.setItem(linha, coluna, QTableWidgetItem(str(valor)))
                coluna += 1
            linha += 1

    def populate_consultas_ativas_medico(self, main_window, consultas_ativas):
        main_window.tb_consulta_agendada.setRowCount(0)
        main_window.tb_consulta_agendada.setRowCount(len(consultas_ativas))
        linha = 0
        for consulta in consultas_ativas:
            coluna = 0
            for valor in consulta:
                main_window.tb_consulta_agendada.setItem(linha, coluna, QTableWidgetItem(str(valor)))
                coluna += 1
            linha += 1


