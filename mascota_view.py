import sys  
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *
from PyQt6.QtGui import *



class Mascota_view(QMainWindow):

	def __init__(self, parent):
		self.parent = parent
		super().__init__()
		self.inicializarUI()
		self.generar_widgets()

	def inicializarUI(self):
		# nombre = mascota.get_Name()
		# edad = mascota.get_age()
		# raza = mascota.get_breed()
		self.setGeometry(100,100,300,300)
		self.setWindowTitle("Mascota")
	
	def generar_widgets(self):

		self.boton_editar = QPushButton("Editar", self)
		self.boton_editar.setGeometry(50,50,80,90)
		self.boton_editar.resize(65,24)
		self.boton_editar.move(103,200)

		self.boton_eliminar = QPushButton("Eliminar",self)
		self.boton_eliminar.resize(74,24)
		self.boton_eliminar.move(15,200)

		self.boton_dar_baja = QPushButton("Dar de baja", self)
		self.boton_dar_baja.resize(105,24)
		self.boton_dar_baja.move(180,200)


		self.label_name = QLabel("Nombre:", self)
		self.label_edad = QLabel("Edad:", self)
		self.label_edad.move(0, 20)
		self.label_raza = QLabel("Raza:", self)
		self.label_raza.move(0,40)
		self.label_sexo = QLabel("Sexo:", self)
		self.label_sexo.move(0,60)
		self.label_consultas = QLabel("Consultas:", self)
		self.label_consultas.move(0,80)
		#self.boton.setCheckable(True)
		#self.boton.clicked.connect(self.second_window)
		#self.boton.setGeometry(5,2,10,10)


		self.widget = QWidget()


		self.vbox = QVBoxLayout()
		for i in range(50):
			object = QLabel("consulta")
			self.vbox.addWidget(object)
		self.widget.setLayout(self.vbox)
		self.scrollArea = QScrollArea(self.widget)
		self.scrollArea.setObjectName(u"scrollArea")
		self.scrollArea.setGeometry(QRect(110, 100, 281, 101))
		#self.scrollArea.setFocusPolicy(Qt.WheelFocus)
		self.scrollArea.setAutoFillBackground(True)
		self.scrollArea.setWidgetResizable(True)
		self.scrollAreaWidgetContents = QWidget()
		self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
		self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 279, 99))
		self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
		self.verticalScrollBar.setObjectName(u"verticalScrollBar")
		self.verticalScrollBar.setGeometry(QRect(260, 0, 20, 101))
		#self.verticalScrollBar.setFocusPolicy(Qt.WheelFocus)
		self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.show()

		def salir(self):
			self.parent.setEnable(True)
			self.close()