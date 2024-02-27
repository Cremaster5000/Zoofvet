import sys 
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from propietario import *
from buscador import *


class Propietario_view(QMainWindow):

	def __init__(self,parent, propietario):
		self.parent = parent
		self.propietario = propietario
		super().__init__()
		print("creado")
		self.inicializar_UI()
		self.desempaqueta_propietario()
		self.listaMascotas()
		self.show()


	def inicializar_UI(self):
		self.setFixedSize(392, 500)
		self.centralwidget = QWidget(self)

		self.boton_editar = QPushButton("Editar", self)
		self.boton_editar.setGeometry(QRect(151, 420, 78, 25))
  
		self.boton_cancelar = QPushButton("Cancelar", self.centralwidget)
		self.boton_cancelar.setGeometry(QRect(40, 420, 77, 25))
		self.boton_cancelar.clicked.connect(self.boton_cancelar)
  
		self.boton_ok = QPushButton("Ok", self.centralwidget)
		self.boton_ok.setGeometry(QRect(260, 420, 77, 25))
  
		self.label_nombre = QLabel("Nombre:", self.centralwidget)
		self.label_nombre.setGeometry(QRect(21, 61, 60, 17))
		self.label_telefono = QLabel("Telefono:", self.centralwidget)
		self.label_telefono.setGeometry(QRect(21, 111, 65, 17))
		self.label_direccion = QLabel("Dirección:",self.centralwidget)
		self.label_direccion.setGeometry(QRect(21, 161, 68, 17))
		self.label_saldo = QLabel("Salso: $", self.centralwidget)
		self.label_saldo.setGeometry(QRect(20, 330, 67, 17))
		self.label_mascotas = QLabel("Mascotas:", self.centralwidget)
		self.label_mascotas.setGeometry(QRect(21, 211, 68, 17))
		self.edit_nombre = QLineEdit(self.centralwidget)
		self.edit_nombre.setGeometry(QRect(91, 61, 231, 25))
		self.edit_telefono = QLineEdit(self.centralwidget)
		self.edit_telefono.setGeometry(QRect(92, 111, 231, 25))
		self.edit_direccion = QLineEdit(self.centralwidget)
		self.edit_direccion.setGeometry(QRect(90, 161, 231, 25))
		self.label_saldo_2 = QLabel(self.centralwidget)
		self.label_saldo_2.setGeometry(QRect(80, 330, 67, 17))
		self.lista_mascotas = QListView(self.centralwidget)
		self.lista_mascotas.setGeometry(QRect(90, 211, 231, 91))
		self.setCentralWidget(self.centralwidget)
		self.menubar = QMenuBar(self)
		self.menubar.setGeometry(QRect(0, 0, 392, 22))
		self.setMenuBar(self.menubar)
		self.statusbar = QStatusBar(self)
		self.setStatusBar(self.statusbar)


		self.show()
		

	def desempaqueta_propietario(self):
		self.edit_nombre.setText(self.propietario.get_name())
		self.edit_telefono.setText(self.propietario.get_telefono())
		self.edit_direccion.setText(self.propietario.get_direccion())
		buscador_ = Buscador()
		buscador_.buscarMascota()
		
  
	def listaMascotas(self):
		pass

	def ver_mascota(self):
		pass

	def pagar(self):
		pass

	def cancelar(self):
		self.parent.setEnabled(True)
		self.close()
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Propietario_view(None)
    test.show()
    sys.exit(app.exec())
    