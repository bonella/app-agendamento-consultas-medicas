# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agenda_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
                               QTextEdit, QVBoxLayout, QWidget, QAbstractItemView)
import view.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(996, 798)
        icon = QIcon()
        icon.addFile(u":/icon_principal/1062557.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_image_principal = QWidget(self.centralwidget)
        self.widget_image_principal.setObjectName(u"widget_image_principal")
        self.widget_image_principal.setMinimumSize(QSize(150, 150))
        self.widget_image_principal.setLayoutDirection(Qt.LeftToRight)
        self.widget_image_principal.setAutoFillBackground(False)
        self.widget_image_principal.setStyleSheet(u"image: url(:/icon_principal/1062557.png);")

        self.verticalLayout_2.addWidget(self.widget_image_principal)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_cadastro_paciente = QWidget()
        self.tab_cadastro_paciente.setObjectName(u"tab_cadastro_paciente")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_cadastro_paciente)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_esquerda = QWidget(self.tab_cadastro_paciente)
        self.widget_esquerda.setObjectName(u"widget_esquerda")
        self.verticalLayout_11 = QVBoxLayout(self.widget_esquerda)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_nome = QLabel(self.widget_esquerda)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setMinimumSize(QSize(111, 0))

        self.horizontalLayout_2.addWidget(self.lbl_nome)

        self.txt_nome = QLineEdit(self.widget_esquerda)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(206, 0))
        self.txt_nome.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.txt_nome)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_numero_seguro_2 = QLabel(self.widget_esquerda)
        self.lbl_numero_seguro_2.setObjectName(u"lbl_numero_seguro_2")
        self.lbl_numero_seguro_2.setMinimumSize(QSize(111, 0))

        self.horizontalLayout_3.addWidget(self.lbl_numero_seguro_2)

        self.txt_numero_seguro = QLineEdit(self.widget_esquerda)
        self.txt_numero_seguro.setObjectName(u"txt_numero_seguro")
        self.txt_numero_seguro.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.txt_numero_seguro)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_historico_medico = QLabel(self.widget_esquerda)
        self.lbl_historico_medico.setObjectName(u"lbl_historico_medico")
        self.lbl_historico_medico.setMinimumSize(QSize(111, 0))

        self.horizontalLayout_9.addWidget(self.lbl_historico_medico)

        self.txt_historico_medico = QLineEdit(self.widget_esquerda)
        self.txt_historico_medico.setObjectName(u"txt_historico_medico")
        self.txt_historico_medico.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.txt_historico_medico)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_idade = QLabel(self.widget_esquerda)
        self.lbl_idade.setObjectName(u"lbl_idade")
        self.lbl_idade.setMinimumSize(QSize(111, 0))

        self.horizontalLayout_4.addWidget(self.lbl_idade)

        self.txt_idade = QLineEdit(self.widget_esquerda)
        self.txt_idade.setObjectName(u"txt_idade")
        self.txt_idade.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.txt_idade)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_telefone = QLabel(self.widget_esquerda)
        self.lbl_telefone.setObjectName(u"lbl_telefone")
        self.lbl_telefone.setMinimumSize(QSize(111, 0))

        self.horizontalLayout_6.addWidget(self.lbl_telefone)

        self.txt_telefone = QLineEdit(self.widget_esquerda)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.txt_telefone)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_cpf = QLabel(self.widget_esquerda)
        self.lbl_cpf.setObjectName(u"lbl_cpf")
        self.lbl_cpf.setMinimumSize(QSize(111, 0))

        self.horizontalLayout_7.addWidget(self.lbl_cpf)

        self.txt_cpf = QLineEdit(self.widget_esquerda)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.txt_cpf)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_email = QLabel(self.widget_esquerda)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setMinimumSize(QSize(111, 0))

        self.horizontalLayout_5.addWidget(self.lbl_email)

        self.txt_email = QLineEdit(self.widget_esquerda)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.txt_email)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_nome_contato_emergencia = QLabel(self.widget_esquerda)
        self.lbl_nome_contato_emergencia.setObjectName(u"lbl_nome_contato_emergencia")
        self.lbl_nome_contato_emergencia.setMinimumSize(QSize(153, 0))

        self.horizontalLayout_8.addWidget(self.lbl_nome_contato_emergencia)

        self.txt_nome_contanto_emergencia = QLineEdit(self.widget_esquerda)
        self.txt_nome_contanto_emergencia.setObjectName(u"txt_nome_contanto_emergencia")
        self.txt_nome_contanto_emergencia.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.txt_nome_contanto_emergencia)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_contato_emergencia = QLabel(self.widget_esquerda)
        self.lbl_contato_emergencia.setObjectName(u"lbl_contato_emergencia")
        self.lbl_contato_emergencia.setMinimumSize(QSize(153, 0))

        self.horizontalLayout_10.addWidget(self.lbl_contato_emergencia)

        self.txt_contato_emergencia = QLineEdit(self.widget_esquerda)
        self.txt_contato_emergencia.setObjectName(u"txt_contato_emergencia")
        self.txt_contato_emergencia.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.txt_contato_emergencia)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton = QPushButton(self.widget_esquerda)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_19.addWidget(self.pushButton)

        self.btn_editar = QPushButton(self.widget_esquerda)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setEnabled(False)
        self.btn_editar.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_19.addWidget(self.btn_editar)


        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.btn_comfirmar = QPushButton(self.widget_esquerda)
        self.btn_comfirmar.setObjectName(u"btn_comfirmar")
        self.btn_comfirmar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_comfirmar.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.btn_comfirmar)


        self.verticalLayout_11.addLayout(self.verticalLayout)


        self.horizontalLayout_12.addWidget(self.widget_esquerda)

        self.widget_image = QWidget(self.tab_cadastro_paciente)
        self.widget_image.setObjectName(u"widget_image")
        self.widget_image.setMinimumSize(QSize(376, 0))
        self.widget_image.setStyleSheet(u"image: url(:/icon_principal/TelaCadastroPaciente-removebg-preview.png);")

        self.horizontalLayout_12.addWidget(self.widget_image)

        self.tabWidget.addTab(self.tab_cadastro_paciente, "")
        self.tab_agendar_consulta = QWidget()
        self.tab_agendar_consulta.setObjectName(u"tab_agendar_consulta")
        self.horizontalLayout = QHBoxLayout(self.tab_agendar_consulta)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_esquerdo = QWidget(self.tab_agendar_consulta)
        self.widget_esquerdo.setObjectName(u"widget_esquerdo")
        self.verticalLayout_14 = QVBoxLayout(self.widget_esquerdo)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lbl_informe_cpf = QLabel(self.widget_esquerdo)
        self.lbl_informe_cpf.setObjectName(u"lbl_informe_cpf")
        self.lbl_informe_cpf.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_13.addWidget(self.lbl_informe_cpf)

        self.txt_cpf_paciente = QLineEdit(self.widget_esquerdo)
        self.txt_cpf_paciente.setObjectName(u"txt_cpf_paciente")

        self.horizontalLayout_13.addWidget(self.txt_cpf_paciente)

        self.btn_consultar_paciente = QPushButton(self.widget_esquerdo)
        self.btn_consultar_paciente.setObjectName(u"btn_consultar_paciente")
        self.btn_consultar_paciente.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.btn_consultar_paciente)


        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lbl_nome_paciente = QLabel(self.widget_esquerdo)
        self.lbl_nome_paciente.setObjectName(u"lbl_nome_paciente")
        self.lbl_nome_paciente.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_14.addWidget(self.lbl_nome_paciente)

        self.txt_nome_paciente = QLineEdit(self.widget_esquerdo)
        self.txt_nome_paciente.setObjectName(u"txt_nome_paciente")

        self.horizontalLayout_14.addWidget(self.txt_nome_paciente)


        self.verticalLayout_14.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lbl_data_2 = QLabel(self.widget_esquerdo)
        self.lbl_data_2.setObjectName(u"lbl_data_2")
        self.lbl_data_2.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_15.addWidget(self.lbl_data_2)

        self.txt_agendar_data = QLineEdit(self.widget_esquerdo)
        self.txt_agendar_data.setObjectName(u"txt_agendar_data")

        self.horizontalLayout_15.addWidget(self.txt_agendar_data)


        self.verticalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lbl_hora = QLabel(self.widget_esquerdo)
        self.lbl_hora.setObjectName(u"lbl_hora")
        self.lbl_hora.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_16.addWidget(self.lbl_hora)

        self.cb_hora = QComboBox(self.widget_esquerdo)
        self.cb_hora.addItem("")
        self.cb_hora.addItem("")
        self.cb_hora.addItem("")
        self.cb_hora.addItem("")
        self.cb_hora.addItem("")
        self.cb_hora.addItem("")
        self.cb_hora.addItem("")
        self.cb_hora.addItem("")
        self.cb_hora.addItem("")
        self.cb_hora.addItem("")
        self.cb_hora.setObjectName(u"cb_hora")
        self.cb_hora.setMinimumSize(QSize(389, 0))

        self.horizontalLayout_16.addWidget(self.cb_hora)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lbl_medico_2 = QLabel(self.widget_esquerdo)
        self.lbl_medico_2.setObjectName(u"lbl_medico_2")
        self.lbl_medico_2.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_17.addWidget(self.lbl_medico_2)

        self.cb_medico_2 = QComboBox(self.widget_esquerdo)
        self.cb_medico_2.addItem("")
        self.cb_medico_2.setObjectName(u"cb_medico_2")
        self.cb_medico_2.setMinimumSize(QSize(389, 0))
        self.cb_medico_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_17.addWidget(self.cb_medico_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lbl_exame = QLabel(self.widget_esquerdo)
        self.lbl_exame.setObjectName(u"lbl_exame")
        self.lbl_exame.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_18.addWidget(self.lbl_exame)

        self.cb_exame = QComboBox(self.widget_esquerdo)
        self.cb_exame.addItem("")
        self.cb_exame.addItem("")
        self.cb_exame.addItem("")
        self.cb_exame.addItem("")
        self.cb_exame.addItem("")
        self.cb_exame.setObjectName(u"cb_exame")
        self.cb_exame.setMinimumSize(QSize(389, 0))
        self.cb_exame.setEditable(False)

        self.horizontalLayout_18.addWidget(self.cb_exame)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.btn_limpar_paciente = QPushButton(self.widget_esquerdo)
        self.btn_limpar_paciente.setObjectName(u"btn_limpar_paciente")

        self.horizontalLayout_30.addWidget(self.btn_limpar_paciente)

        self.btn_confirmar = QPushButton(self.widget_esquerdo)
        self.btn_confirmar.setObjectName(u"btn_confirmar")

        self.horizontalLayout_30.addWidget(self.btn_confirmar)


        self.verticalLayout_14.addLayout(self.horizontalLayout_30)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.widget_esquerdo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label = QLabel(self.widget_esquerdo)
        self.label.setObjectName(u"label")

        self.horizontalLayout_31.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(self.widget_esquerdo)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_31.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.widget_esquerdo)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_31.addWidget(self.pushButton_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_31)


        self.verticalLayout_14.addLayout(self.verticalLayout_10)

        self.btn_reagendar = QPushButton(self.widget_esquerdo)
        self.btn_reagendar.setObjectName(u"btn_reagendar")
        self.btn_reagendar.setEnabled(False)

        self.verticalLayout_14.addWidget(self.btn_reagendar)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_cancelar_consulta = QPushButton(self.widget_esquerdo)
        self.btn_cancelar_consulta.setObjectName(u"btn_cancelar_consulta")
        self.btn_cancelar_consulta.setEnabled(False)

        self.verticalLayout_5.addWidget(self.btn_cancelar_consulta)

        self.cb_cancelamento = QComboBox(self.widget_esquerdo)
        self.cb_cancelamento.addItem("")
        self.cb_cancelamento.addItem("")
        self.cb_cancelamento.addItem("")
        self.cb_cancelamento.addItem("")
        self.cb_cancelamento.addItem("")
        self.cb_cancelamento.setObjectName(u"cb_cancelamento")
        self.cb_cancelamento.setEnabled(False)

        self.verticalLayout_5.addWidget(self.cb_cancelamento)


        self.verticalLayout_14.addLayout(self.verticalLayout_5)


        self.horizontalLayout.addWidget(self.widget_esquerdo)

        self.widget_direito = QWidget(self.tab_agendar_consulta)
        self.widget_direito.setObjectName(u"widget_direito")
        self.verticalLayout_8 = QVBoxLayout(self.widget_direito)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_informacoes = QLabel(self.widget_direito)
        self.lbl_informacoes.setObjectName(u"lbl_informacoes")
        self.lbl_informacoes.setMaximumSize(QSize(16777215, 70))
        self.lbl_informacoes.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.lbl_informacoes)

        self.txt_informacoes_adicionais = QTextEdit(self.widget_direito)
        self.txt_informacoes_adicionais.setObjectName(u"txt_informacoes_adicionais")

        self.verticalLayout_4.addWidget(self.txt_informacoes_adicionais)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.widget_direito)

        self.tabWidget.addTab(self.tab_agendar_consulta, "")
        self.tab_consultas_agendadas = QWidget()
        self.tab_consultas_agendadas.setObjectName(u"tab_consultas_agendadas")
        self.horizontalLayout_20 = QHBoxLayout(self.tab_consultas_agendadas)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.widget_esquerdo_2 = QWidget(self.tab_consultas_agendadas)
        self.widget_esquerdo_2.setObjectName(u"widget_esquerdo_2")
        self.widget_esquerdo_2.setMinimumSize(QSize(0, 0))
        self.widget_esquerdo_2.setMaximumSize(QSize(208, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.widget_esquerdo_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_medico = QLabel(self.widget_esquerdo_2)
        self.lbl_medico.setObjectName(u"lbl_medico")
        self.lbl_medico.setMaximumSize(QSize(55, 40))

        self.horizontalLayout_11.addWidget(self.lbl_medico)

        self.cb_medico = QComboBox(self.widget_esquerdo_2)
        self.cb_medico.addItem("")
        self.cb_medico.setObjectName(u"cb_medico")
        self.cb_medico.setEnabled(True)
        self.cb_medico.setMinimumSize(QSize(130, 0))
        self.cb_medico.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_11.addWidget(self.cb_medico)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.lbl_oue = QLabel(self.widget_esquerdo_2)
        self.lbl_oue.setObjectName(u"lbl_oue")
        self.lbl_oue.setMaximumSize(QSize(186, 20))

        self.verticalLayout_9.addWidget(self.lbl_oue)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lbl_data = QLabel(self.widget_esquerdo_2)
        self.lbl_data.setObjectName(u"lbl_data")
        self.lbl_data.setMaximumSize(QSize(55, 40))

        self.horizontalLayout_21.addWidget(self.lbl_data)

        self.lineEdit = QLineEdit(self.widget_esquerdo_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(70, 0))
        self.lineEdit.setMaximumSize(QSize(130, 25))

        self.horizontalLayout_21.addWidget(self.lineEdit)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)


        self.verticalLayout_13.addLayout(self.verticalLayout_9)

        self.btn_diario = QPushButton(self.widget_esquerdo_2)
        self.btn_diario.setObjectName(u"btn_diario")
        self.btn_diario.setMinimumSize(QSize(0, 0))
        self.btn_diario.setMaximumSize(QSize(186, 16777215))
        self.btn_diario.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.btn_diario)

        self.btn_semanal = QPushButton(self.widget_esquerdo_2)
        self.btn_semanal.setObjectName(u"btn_semanal")
        self.btn_semanal.setMaximumSize(QSize(186, 16777215))
        self.btn_semanal.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.btn_semanal)

        self.btn_mensal = QPushButton(self.widget_esquerdo_2)
        self.btn_mensal.setObjectName(u"btn_mensal")
        self.btn_mensal.setMaximumSize(QSize(186, 16777215))
        self.btn_mensal.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.btn_mensal)

        self.btn_consultar = QPushButton(self.widget_esquerdo_2)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setMinimumSize(QSize(0, 50))
        self.btn_consultar.setMaximumSize(QSize(186, 16777215))
        self.btn_consultar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consultar.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.btn_consultar)


        self.horizontalLayout_20.addWidget(self.widget_esquerdo_2)

        self.widget_direito_3 = QWidget(self.tab_consultas_agendadas)
        self.widget_direito_3.setObjectName(u"widget_direito_3")
        self.widget_direito_3.setMinimumSize(QSize(731, 567))
        self.verticalLayout_6 = QVBoxLayout(self.widget_direito_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_exames = QLabel(self.widget_direito_3)
        self.lbl_exames.setObjectName(u"lbl_exames")
        self.lbl_exames.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.lbl_exames)

        self.tb_consulta_agendada = QTableWidget(self.widget_direito_3)
        if (self.tb_consulta_agendada.columnCount() < 5):
            self.tb_consulta_agendada.setColumnCount(5)
        header_tb_consulta_agendada = self.tb_consulta_agendada.horizontalHeader()
        header_tb_consulta_agendada.setSectionResizeMode(QHeaderView.Stretch)
        self.tb_consulta_agendada.verticalHeader().hide()
        # self.tb_consulta_agendada.setSelectionBehavior(QTableWidget.SelectRows)
        self.tb_consulta_agendada.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tb_consulta_agendada.setSelectionMode(QAbstractItemView.SingleSelection)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_consulta_agendada.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_consulta_agendada.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_consulta_agendada.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_consulta_agendada.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_consulta_agendada.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tb_consulta_agendada.setObjectName(u"tb_consulta_agendada")
        self.tb_consulta_agendada.setMinimumSize(QSize(0, 0))
        self.tb_consulta_agendada.setMaximumSize(QSize(16777215, 16777215))
        self.tb_consulta_agendada.horizontalHeader().setCascadingSectionResizes(False)

        self.tb_consulta_agendada.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_consulta_agendada.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tb_consulta_agendada)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)


        self.horizontalLayout_20.addWidget(self.widget_direito_3)

        self.tabWidget.addTab(self.tab_consultas_agendadas, "")
        self.tab_gestao = QWidget()
        self.tab_gestao.setObjectName(u"tab_gestao")
        self.horizontalLayout_22 = QHBoxLayout(self.tab_gestao)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.widget_5 = QWidget(self.tab_gestao)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lbl_cadastrar_medico = QLabel(self.widget_5)
        self.lbl_cadastrar_medico.setObjectName(u"lbl_cadastrar_medico")
        self.lbl_cadastrar_medico.setMinimumSize(QSize(0, 0))
        self.lbl_cadastrar_medico.setMaximumSize(QSize(16777215, 20))
        self.lbl_cadastrar_medico.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.lbl_cadastrar_medico)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lbl_nome_medico = QLabel(self.widget_5)
        self.lbl_nome_medico.setObjectName(u"lbl_nome_medico")
        self.lbl_nome_medico.setMinimumSize(QSize(82, 0))

        self.horizontalLayout_24.addWidget(self.lbl_nome_medico)

        self.txt_nome_medico = QLineEdit(self.widget_5)
        self.txt_nome_medico.setObjectName(u"txt_nome_medico")

        self.horizontalLayout_24.addWidget(self.txt_nome_medico)


        self.verticalLayout_12.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lbl_especialidade_medico = QLabel(self.widget_5)
        self.lbl_especialidade_medico.setObjectName(u"lbl_especialidade_medico")
        self.lbl_especialidade_medico.setMinimumSize(QSize(82, 0))

        self.horizontalLayout_23.addWidget(self.lbl_especialidade_medico)

        self.txt_especialidade_medico = QLineEdit(self.widget_5)
        self.txt_especialidade_medico.setObjectName(u"txt_especialidade_medico")

        self.horizontalLayout_23.addWidget(self.txt_especialidade_medico)


        self.verticalLayout_12.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lbl_telefone_medico = QLabel(self.widget_5)
        self.lbl_telefone_medico.setObjectName(u"lbl_telefone_medico")
        self.lbl_telefone_medico.setMinimumSize(QSize(82, 0))

        self.horizontalLayout_25.addWidget(self.lbl_telefone_medico)

        self.txt_telefone_medico = QLineEdit(self.widget_5)
        self.txt_telefone_medico.setObjectName(u"txt_telefone_medico")

        self.horizontalLayout_25.addWidget(self.txt_telefone_medico)


        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lbl_email_medico = QLabel(self.widget_5)
        self.lbl_email_medico.setObjectName(u"lbl_email_medico")
        self.lbl_email_medico.setMinimumSize(QSize(82, 0))

        self.horizontalLayout_29.addWidget(self.lbl_email_medico)

        self.txt_email_medico = QLineEdit(self.widget_5)
        self.txt_email_medico.setObjectName(u"txt_email_medico")

        self.horizontalLayout_29.addWidget(self.txt_email_medico)


        self.verticalLayout_12.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lbl_numero_crm = QLabel(self.widget_5)
        self.lbl_numero_crm.setObjectName(u"lbl_numero_crm")
        self.lbl_numero_crm.setMinimumSize(QSize(82, 0))

        self.horizontalLayout_28.addWidget(self.lbl_numero_crm)

        self.txt_numero_crm = QLineEdit(self.widget_5)
        self.txt_numero_crm.setObjectName(u"txt_numero_crm")

        self.horizontalLayout_28.addWidget(self.txt_numero_crm)


        self.verticalLayout_12.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lbl_idade_medico = QLabel(self.widget_5)
        self.lbl_idade_medico.setObjectName(u"lbl_idade_medico")
        self.lbl_idade_medico.setMinimumSize(QSize(82, 0))

        self.horizontalLayout_26.addWidget(self.lbl_idade_medico)

        self.txt_idade_medico = QLineEdit(self.widget_5)
        self.txt_idade_medico.setObjectName(u"txt_idade_medico")

        self.horizontalLayout_26.addWidget(self.txt_idade_medico)


        self.verticalLayout_12.addLayout(self.horizontalLayout_26)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.btn_consultar_medico = QPushButton(self.widget_5)
        self.btn_consultar_medico.setObjectName(u"btn_consultar_medico")

        self.horizontalLayout_27.addWidget(self.btn_consultar_medico)

        self.btn_editar_medico = QPushButton(self.widget_5)
        self.btn_editar_medico.setObjectName(u"btn_editar_medico")
        self.btn_editar_medico.setEnabled(False)

        self.horizontalLayout_27.addWidget(self.btn_editar_medico)


        self.verticalLayout_7.addLayout(self.horizontalLayout_27)

        self.btn_confirmar_medico = QPushButton(self.widget_5)
        self.btn_confirmar_medico.setObjectName(u"btn_confirmar_medico")

        self.verticalLayout_7.addWidget(self.btn_confirmar_medico)


        self.verticalLayout_12.addLayout(self.verticalLayout_7)


        self.horizontalLayout_22.addWidget(self.widget_5)

        self.widget_image_gestao = QWidget(self.tab_gestao)
        self.widget_image_gestao.setObjectName(u"widget_image_gestao")
        self.widget_image_gestao.setMinimumSize(QSize(350, 392))
        self.widget_image_gestao.setMaximumSize(QSize(480, 480))
        self.widget_image_gestao.setStyleSheet(u"image: url(:/icon_principal/medico.png);")

        self.horizontalLayout_22.addWidget(self.widget_image_gestao)

        self.tabWidget.addTab(self.tab_gestao, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Agendamento", None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nome:</p></body></html>", None))
        self.lbl_numero_seguro_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>N\u00famero do seguro:</p></body></html>", None))
        self.txt_numero_seguro.setInputMask("")
        self.lbl_historico_medico.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Hist\u00f3rico m\u00e9dico:</p></body></html>", None))
        self.lbl_idade.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Idade:</p></body></html>", None))
        self.lbl_telefone.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Telefone:</p></body></html>", None))
        self.lbl_cpf.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>CPF:</p></body></html>", None))
        self.lbl_email.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>E-mail:</p></body></html>", None))
        self.lbl_nome_contato_emergencia.setText(QCoreApplication.translate("MainWindow", u"Nome contato de emerg\u00eancia:", None))
        self.lbl_contato_emergencia.setText(QCoreApplication.translate("MainWindow", u"Contato de emerg\u00eancia:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_comfirmar.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cadastro_paciente), QCoreApplication.translate("MainWindow", u"Cadastro Paciente", None))
        self.lbl_informe_cpf.setText(QCoreApplication.translate("MainWindow", u"Informe CPF:", None))
        self.btn_consultar_paciente.setText(QCoreApplication.translate("MainWindow", u"Consultar Paciente", None))
        self.lbl_nome_paciente.setText(QCoreApplication.translate("MainWindow", u"Nome paciente:", None))
        self.lbl_data_2.setText(QCoreApplication.translate("MainWindow", u"Data:", None))
        self.txt_agendar_data.setInputMask(QCoreApplication.translate("MainWindow", u"99/99/9999;_", None))
        self.lbl_hora.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Hora:</p></body></html>", None))
        self.cb_hora.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione um hor\u00e1rio", None))
        self.cb_hora.setItemText(1, QCoreApplication.translate("MainWindow", u"08:00", None))
        self.cb_hora.setItemText(2, QCoreApplication.translate("MainWindow", u"09:00", None))
        self.cb_hora.setItemText(3, QCoreApplication.translate("MainWindow", u"10:00", None))
        self.cb_hora.setItemText(4, QCoreApplication.translate("MainWindow", u"11:00", None))
        self.cb_hora.setItemText(5, QCoreApplication.translate("MainWindow", u"13:00", None))
        self.cb_hora.setItemText(6, QCoreApplication.translate("MainWindow", u"14:00", None))
        self.cb_hora.setItemText(7, QCoreApplication.translate("MainWindow", u"15:00", None))
        self.cb_hora.setItemText(8, QCoreApplication.translate("MainWindow", u"16:00", None))
        self.cb_hora.setItemText(9, QCoreApplication.translate("MainWindow", u"17:00", None))

#if QT_CONFIG(accessibility)
        self.cb_hora.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.cb_hora.setCurrentText(QCoreApplication.translate("MainWindow", u"Selecione um hor\u00e1rio", None))
        self.lbl_medico_2.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dico:", None))
        self.cb_medico_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione um profissional", None))

        self.cb_medico_2.setCurrentText(QCoreApplication.translate("MainWindow", u"Selecione um profissional", None))
        self.lbl_exame.setText(QCoreApplication.translate("MainWindow", u"Consulta", None))
        self.cb_exame.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione um tipo de consulta", None))
        self.cb_exame.setItemText(1, QCoreApplication.translate("MainWindow", u"Rotina", None))
        self.cb_exame.setItemText(2, QCoreApplication.translate("MainWindow", u"Acompanhamento", None))
        self.cb_exame.setItemText(3, QCoreApplication.translate("MainWindow", u"Pr\u00e9-natal", None))
        self.cb_exame.setItemText(4, QCoreApplication.translate("MainWindow", u"Puericultura", None))

        self.cb_exame.setCurrentText(QCoreApplication.translate("MainWindow", u"Selecione um tipo de consulta", None))
        self.btn_limpar_paciente.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_confirmar.setText(QCoreApplication.translate("MainWindow", u"Confirmar ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Gerenciar Consulta</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Informe Protocolo:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Consultar Protocolo", None))
        self.btn_reagendar.setText(QCoreApplication.translate("MainWindow", u"Reagendar Consulta", None))
        self.btn_cancelar_consulta.setText(QCoreApplication.translate("MainWindow", u"Cancelar Consulta", None))
        self.cb_cancelamento.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione o motivo", None))
        self.cb_cancelamento.setItemText(1, QCoreApplication.translate("MainWindow", u"Desist\u00eancia", None))
        self.cb_cancelamento.setItemText(2, QCoreApplication.translate("MainWindow", u"Atraso", None))
        self.cb_cancelamento.setItemText(3, QCoreApplication.translate("MainWindow", u"N\u00e3o comparecimento", None))
        self.cb_cancelamento.setItemText(4, QCoreApplication.translate("MainWindow", u"Falecimento", None))

        self.lbl_informacoes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Informa\u00e7\u00f5es Adicionais</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_agendar_consulta), QCoreApplication.translate("MainWindow", u"Gest\u00e3o de Consultas", None))
        self.lbl_medico.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dico:", None))
        self.cb_medico.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione um m\u00e9dico", None))

        self.cb_medico.setCurrentText(QCoreApplication.translate("MainWindow", u"Selecione um m\u00e9dico", None))
        self.lbl_oue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">e/ou</p></body></html>", None))
        self.lbl_data.setText(QCoreApplication.translate("MainWindow", u"Data:", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("MainWindow", u"99/99/9999;_", None))
        self.btn_diario.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1rio", None))
        self.btn_semanal.setText(QCoreApplication.translate("MainWindow", u"Semanal", None))
        self.btn_mensal.setText(QCoreApplication.translate("MainWindow", u"Mensal", None))
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.lbl_exames.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Exames</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_consulta_agendada.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"N\u00famero Protocolo", None));
        ___qtablewidgetitem1 = self.tb_consulta_agendada.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Data/Hora", None));
        ___qtablewidgetitem2 = self.tb_consulta_agendada.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Paciente", None));
        ___qtablewidgetitem3 = self.tb_consulta_agendada.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem4 = self.tb_consulta_agendada.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dico", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_consultas_agendadas), QCoreApplication.translate("MainWindow", u"Consultas Agendadas", None))
        self.lbl_cadastrar_medico.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Cadastrar M\u00e9dico</span></p></body></html>", None))
        self.lbl_nome_medico.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.lbl_especialidade_medico.setText(QCoreApplication.translate("MainWindow", u"Especialidade:", None))
        self.lbl_telefone_medico.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.lbl_email_medico.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lbl_numero_crm.setText(QCoreApplication.translate("MainWindow", u"N\u00famero CRM:", None))
        self.lbl_idade_medico.setText(QCoreApplication.translate("MainWindow", u"Idade:", None))
        self.btn_consultar_medico.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.btn_editar_medico.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_confirmar_medico.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gestao), QCoreApplication.translate("MainWindow", u"Gest\u00e3o ", None))
    # retranslateUi

