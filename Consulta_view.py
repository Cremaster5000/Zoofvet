
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import datetime

import sys


class Consulta_View(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
        
    def setupUi(self):
        self.setGeometry(QRect(0,0,639,650))
        self.setMaximumSize(639, 650)
        self.setWindowTitle("Consulta")
        self.centralwidget = QWidget(self)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QRect(0, 0, 637, 648))
        self.EFG = QWidget()
        self.widget = QWidget(self.EFG)
        self.widget.setGeometry(QRect(40, 420, 571, 171))
        self.formLayout_17 = QFormLayout(self.widget)
        self.formLayout_17.setContentsMargins(0, 0, 0, 35)
        self.label_12 = QLabel("Anamnesis:", self.widget)

        self.formLayout_17.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.edit_anamnesis = QTextEdit(self.widget)

        self.formLayout_17.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.edit_anamnesis)

        self.widget1 = QWidget(self.EFG)
        self.widget1.setGeometry(QRect(50, 20, 201, 19))
        self.formLayout = QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_paciente = QLabel(self.widget1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_paciente)

        self.label = QLabel("Paciente:", self.widget1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.widget2 = QWidget(self.EFG)
        self.widget2.setGeometry(QRect(460, 20, 141, 19))
        self.formLayout_2 = QFormLayout(self.widget2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel("Fecha:", self.widget2)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_fecha = QLabel(self.widget2)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_fecha)

        self.widget3 = QWidget(self.EFG)
        self.widget3.setGeometry(QRect(80, 90, 91, 27))
        self.formLayout_3 = QFormLayout(self.widget3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel("FC:", self.widget3)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.edit_fc = QLineEdit(self.widget3)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_fc)

        self.widget4 = QWidget(self.EFG)
        self.widget4.setGeometry(QRect(280, 90, 101, 27))
        self.formLayout_4 = QFormLayout(self.widget4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel("FR:", self.widget4)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.edit_fr = QLineEdit(self.widget4)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_fr)

        self.widget5 = QWidget(self.EFG)
        self.widget5.setGeometry(QRect(290, 130, 121, 27))
        self.formLayout_5 = QFormLayout(self.widget5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel("RT:", self.widget5)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.combobox_rt = QComboBox(self.widget5)
        self.combobox_rt.addItem("Positivo")
        self.combobox_rt.addItem("Negativo")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_rt)

        self.widget6 = QWidget(self.EFG)
        self.widget6.setGeometry(QRect(460, 90, 111, 27))
        self.formLayout_6 = QFormLayout(self.widget6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.edit_tc = QLineEdit(self.widget6)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_tc)

        self.label_5 = QLabel("TC:", self.widget6)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.widget7 = QWidget(self.EFG)
        self.widget7.setGeometry(QRect(470, 130, 124, 27))
        self.formLayout_7 = QFormLayout(self.widget7)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel("RD:", self.widget7)

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.combobox_rd = QComboBox(self.widget7)
        self.combobox_rd.addItem("Positivo")
        self.combobox_rd.addItem("Negativo")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_rd)

        self.widget8 = QWidget(self.EFG)
        self.widget8.setGeometry(QRect(50, 130, 210, 27))
        self.formLayout_8 = QFormLayout(self.widget8)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel("Edo. Mental:", self.widget8)

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.combobox_emental = QComboBox(self.widget8)
        self.combobox_emental.adjustSize()
        self.combobox_emental.addItem("Alerta")
        self.combobox_emental.addItem("Comatoso")
        self.combobox_emental.addItem("Estupor")
        self.combobox_emental.addItem("Desorientado")
        self.combobox_emental.addItem("Deprimido")
        self.combobox_emental.addItem("Exitado")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_emental)

        self.widget9 = QWidget(self.EFG)
        self.widget9.setGeometry(QRect(40, 190, 281, 27))
        self.formLayout_9 = QFormLayout(self.widget9)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel("Auscultación cardiaca:", self.widget9)

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.combobox_ac = QComboBox(self.widget9)
        self.combobox_ac.addItem("Normal")
        self.combobox_ac.addItem("Soplo")
        self.combobox_ac.addItem("Arritmia")
        self.combobox_ac.addItem("Bradicardia")
        self.combobox_ac.addItem("Taquicardia")

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_ac)

        self.widget10 = QWidget(self.EFG)
        self.widget10.setGeometry(QRect(360, 190, 251, 27))
        self.formLayout_10 = QFormLayout(self.widget10)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel("Linfonodos:", self.widget10)

        self.formLayout_10.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.edit_linfo = QLineEdit(self.widget10)

        self.formLayout_10.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_linfo)

        self.widget11 = QWidget(self.EFG)
        self.widget11.setGeometry(QRect(40, 240, 270, 27))
        self.formLayout_11 = QFormLayout(self.widget11)
        self.formLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel("Auscultación pulmonar:", self.widget11)

        self.formLayout_11.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.combobox_ap = QComboBox(self.widget11)
        self.combobox_ap.addItem("Normal")
        self.combobox_ap.addItem("Reducido")
        self.combobox_ap.addItem("Liquido")
        self.combobox_ap.addItem("Sibilancias")
        self.combobox_ap.addItem("Estertor")
        self.combobox_ap.addItem("Estridor")
        self.combobox_ap.addItem("Roncus")


        self.formLayout_11.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_ap)

        self.widget12 = QWidget(self.EFG)
        self.widget12.setGeometry(QRect(340, 240, 276, 27))
        self.formLayout_12 = QFormLayout(self.widget12)
        self.formLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel("Palpación abdominal:", self.widget12)

        self.formLayout_12.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.combobox_palpacion = QComboBox(self.widget12)
        self.combobox_palpacion.addItem("Sin dolor")
        self.combobox_palpacion.addItem("Dolor")
        self.combobox_palpacion.addItem("Gas")
        self.combobox_palpacion.addItem("Gas con dolor")
        self.combobox_palpacion.addItem("Líquido")
        self.combobox_palpacion.addItem("Ocupado")

        self.formLayout_12.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_palpacion)

        self.widget13 = QWidget(self.EFG)
        self.widget13.setGeometry(QRect(300, 20, 111, 19))
        self.formLayout_13 = QFormLayout(self.widget13)
        self.formLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel("Sexo:", self.widget13)

        self.formLayout_13.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_16)

        self.label_sexo = QLabel(self.widget13)

        self.formLayout_13.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_sexo)

        self.widget14 = QWidget(self.EFG)
        self.widget14.setGeometry(QRect(50, 50, 111, 19))
        self.formLayout_14 = QFormLayout(self.widget14)
        self.formLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel("Edad:", self.widget14)

        self.formLayout_14.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.label_edad = QLabel(self.widget14)

        self.formLayout_14.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_edad)

        self.widget15 = QWidget(self.EFG)
        self.widget15.setGeometry(QRect(200, 50, 131, 19))
        self.formLayout_15 = QFormLayout(self.widget15)
        self.formLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel("Raza:", self.widget15)

        self.formLayout_15.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_17)

        self.label_raza = QLabel(self.widget15)

        self.formLayout_15.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_raza)

        self.widget16 = QWidget(self.EFG)
        self.widget16.setGeometry(QRect(40, 300, 571, 101))
        self.formLayout_16 = QFormLayout(self.widget16)
        self.formLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel("Historia clínica:", self.widget16)

        self.formLayout_16.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.edit_historia = QTextEdit(self.widget16)

        self.formLayout_16.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.edit_historia)

        self.widget17 = QWidget(self.EFG)
        self.widget17.setGeometry(QRect(380, 50, 159, 19))
        self.formLayout_26 = QFormLayout(self.widget17)
        self.formLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel("Esterilizado:", self.widget17)

        self.formLayout_26.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.label_esterilizado = QLabel(self.widget17)

        self.formLayout_26.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_esterilizado)

        self.tabWidget.addTab(self.EFG, "EFG")
        self.DX = QWidget()
        
        self.boton_imprimir = QPushButton("Imprimir receta", self.DX)
        self.boton_imprimir.setGeometry(QRect(500, 540, 113, 25))
        self.boton_imprimir.clicked.connect(self.imprimir_receta)
        self.boton_cancelar = QPushButton("Cancelar", self.DX)
        self.boton_cancelar.setGeometry(QRect(50, 540, 89, 25))
        self.boton_cancelar.clicked.connect(self.cancelar)
        self.boton_guardar = QPushButton("Guardar", self.DX)
        self.boton_guardar.setGeometry(QRect(280, 540, 89, 25))
        self.boton_guardar.clicked.connect(self.guardar)
        self.widget18 = QWidget(self.DX)
        self.widget18.setGeometry(QRect(370, 100, 241, 27))
        self.formLayout_18 = QFormLayout(self.widget18)
        self.formLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel("Laboratorio:", self.widget18)

        self.formLayout_18.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_21)

        self.editlaboratorio = QLineEdit(self.widget18)

        self.formLayout_18.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editlaboratorio)

        self.widget19 = QWidget(self.DX)
        self.widget19.setGeometry(QRect(40, 150, 271, 121))
        self.formLayout_19 = QFormLayout(self.widget19)
        self.formLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel("Diagnosticos diferenciales:", self.widget19)

        self.formLayout_19.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_22)

        self.edit_diferenciales = QTextEdit(self.widget19)

        self.formLayout_19.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.edit_diferenciales)

        self.widget20 = QWidget(self.DX)
        self.widget20.setGeometry(QRect(370, 40, 241, 27))
        self.formLayout_20 = QFormLayout(self.widget20)
        self.formLayout_20.setContentsMargins(0, 0, 0, 0)
        self.edit_muestras = QLineEdit(self.widget20)

        self.formLayout_20.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_muestras)

        self.label_20 = QLabel("Muestras:", self.widget20)

        self.formLayout_20.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_20)

        self.widget21 = QWidget(self.DX)
        self.widget21.setGeometry(QRect(40, 100, 231, 27))
        self.formLayout_21 = QFormLayout(self.widget21)
        self.formLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel("Lesiones:", self.widget21)

        self.formLayout_21.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_19)

        self.edit_lesiones = QLineEdit(self.widget21)

        self.formLayout_21.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_lesiones)

        self.widget22 = QWidget(self.DX)
        self.widget22.setGeometry(QRect(40, 40, 201, 27))
        self.formLayout_22 = QFormLayout(self.widget22)
        self.formLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel("Copro:", self.widget22)

        self.formLayout_22.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_18)

        self.edit_copro = QLineEdit(self.widget22)

        self.formLayout_22.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_copro)

        self.widget23 = QWidget(self.DX)
        self.widget23.setGeometry(QRect(350, 150, 264, 121))
        self.formLayout_23 = QFormLayout(self.widget23)
        self.formLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel("Pruebas adicionales:", self.widget23)

        self.formLayout_23.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_23)

        self.textEdit = QTextEdit(self.widget23)

        self.formLayout_23.setWidget(1, QFormLayout.ItemRole.LabelRole, self.textEdit)

        self.widget24 = QWidget(self.DX)
        self.widget24.setGeometry(QRect(350, 310, 197, 28))
        self.formLayout_24 = QFormLayout(self.widget24)
        #self.formLayout_24.setGeometry(QRect(350, 310, 197, 28))
        self.formLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel("Próxima visita:")

        self.dateEdit = QDateEdit(self.widget24)
               
        self.dateEdit.setDate(datetime.date.today())
        self.dateEdit.setCalendarPopup(True)
        
        #self.formLayout_24.addRow(self.label_25, self.dateEdit)
        self.formLayout_24.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_25)
        self.formLayout_24.setWidget(0, QFormLayout.ItemRole.FieldRole, self.dateEdit)

        self.widget25 = QWidget(self.DX)
        self.widget25.setGeometry(QRect(40, 318, 571, 198))
        self.formLayout_25 = QFormLayout(self.widget25)
        self.formLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel("Tratamiento:", self.widget25)

        self.formLayout_25.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.textEdit_2 = QTextEdit(self.widget25)

        self.formLayout_25.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.textEdit_2)

        self.tabWidget.addTab(self.DX, "DX")
        self.setCentralWidget(self.centralwidget)
        self.tabWidget.raise_()
        self.label_7.raise_()
        self.combobox_rd.raise_()
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.tabWidget.setCurrentIndex(0)
        
    def cancelar(self):
        self.parent.setEnable(True)
        self.close()
        
    def guardar(self):
        pass
    
    def imprimir_receta(self):
        pass


    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    test = Consulta_View()
    sys.exit(app.exec())

