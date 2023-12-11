import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPalette, QColor, Qt

from view.main_ui import Ui_MainWindow

from services.main_window_service import MainWindowService
from services.paciente_service import PacienteService
from services.medico_service import MedicoService
from services.consulta_service import ConsultaService

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # Ajustes iniciais do sistema
        tema = True
        self.txt_nome_paciente.setReadOnly(True)
        self.paciente_service = PacienteService()
        self.medico_service = MedicoService()
        self.consulta_service = ConsultaService()
        self.main_window_service = MainWindowService()

        self.definir_tema(tema)
        self.main_window_service.populate_combo_medicos(self)
        self.main_window_service.populate_combo_medicos_agendamento(self)
        self.main_window_service.populate_consultas_ativas(self)

        self.btn_confirmar_medico.clicked.connect(self.adicionar_medico)
        self.btn_editar_medico.clicked.connect(self.atualizar_medico)
        self.btn_consultar_medico.clicked.connect(self.consultar_medico)

        self.btn_comfirmar.clicked.connect(self.adicionar_paciente)
        self.btn_editar.clicked.connect(self.atualizar_paciente)
        self.pushButton.clicked.connect(self.consultar_paciente)

        self.btn_consultar_paciente.clicked.connect(self.consultar_paciente_agenda)
        self.btn_limpar_paciente.clicked.connect(self.limpar_dados)
        self.btn_confirmar.clicked.connect(self.adicionar_consulta)
        self.btn_consultar.clicked.connect(self.buscar_consultas_agendadas)
        self.btn_diario.clicked.connect(self.buscar_consultas_agendadas_diario)
        self.btn_semanal.clicked.connect(self.buscar_consultas_agendadas_semana)
        self.btn_mensal.clicked.connect(self.buscar_consultas_agendadas_mensal)

        self.pushButton_2.clicked.connect(self.buscar_consulta_protocolo)
        self.btn_reagendar.clicked.connect(self.reagendar_consulta)
        self.btn_cancelar_consulta.clicked.connect(self.cancelar_consulta)

    def adicionar_paciente(self):
        self.paciente_service.insert_paciente(self)

    def atualizar_paciente(self):
        self.paciente_service.update_paciente(self)

    def consultar_paciente(self):
        self.paciente_service.select_paciente_consulta(self)

    def adicionar_medico(self):
        self.medico_service.insert_medico(self)

    def atualizar_medico(self):
        self.medico_service.update_medico(self)

    def consultar_medico(self):
        self.medico_service.select_medico_consulta(self)

    def consultar_paciente_agenda(self):
        self.consulta_service.select_paciente_agenda(self)

    def adicionar_consulta(self):
        self.consulta_service.insert_consulta(self)

    def limpar_dados(self):
        self.consulta_service.limpar_agendamento_consulta(self)

    def buscar_consultas_agendadas(self):
        self.consulta_service.select_consultas_agendadas(self)

    def buscar_consultas_agendadas_diario(self):
        self.consulta_service.select_consultas_dia(self)

    def buscar_consultas_agendadas_semana(self):
        self.consulta_service.select_consultas_semana(self)

    def buscar_consultas_agendadas_mensal(self):
        self.consulta_service.select_consultas_mes(self)

    def buscar_consulta_protocolo(self):
        self.consulta_service.select_consulta_por_protocolo(self)

    def reagendar_consulta(self):
        self.consulta_service.update_consulta_reagendar(self)

    def cancelar_consulta(self):
        self.consulta_service.update_consulta_cancelar(self)

    # Definir tema
    def definir_tema(self, tema):
        if tema is False:
            palette = QPalette()
            palette.setColor(QPalette.ColorRole.Window, QColor(50, 50, 50))
            palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Base, QColor(45, 45, 45))
            palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(70, 70, 70))
            palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))
            palette.setColor(QPalette.ColorRole.Shadow, QColor(25, 25, 25))
            palette.setColor(QPalette.ColorRole.AlternateBase, QColor(55, 55, 55))
            palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Button, QColor(50, 50, 50))
            palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
            palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
            app.setPalette(palette)
            app.setStyle('Fusion')
        else:
            palette = QPalette()
            palette.setColor(QPalette.ColorRole.Window, QColor(240, 240, 240))
            palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.black)
            palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
            palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.black)
            palette.setColor(QPalette.ColorRole.Dark, QColor(200, 200, 200))
            palette.setColor(QPalette.ColorRole.Shadow, QColor(180, 180, 180))
            palette.setColor(QPalette.ColorRole.AlternateBase, QColor(240, 240, 240))
            palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.black)
            palette.setColor(QPalette.ColorRole.Button, QColor(240, 240, 240))
            palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.black)
            palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
            palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.ColorRole.HighlightedText, QColor(240, 240, 240))
            app.setPalette(palette)
            app.setStyle('Fusion')

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())