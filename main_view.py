import sys  
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from busqueda_view import Busqueda_view
from propietario_view import Propietario_view

class Main_view(QMainWindow):
	def __init__(self):
		super().__init__()
		self.inicializar_UI()
		self.show()


	def inicializar_UI(self):
		self.setWindowTitle("ZoofVet 0.01")
		self.setGeometry(100,100,800,600)
		#self.setObjectName(u"self")
		self.actionActualizar_informacion = QAction("Actualizar información", self)
		
		self.actionImprimir_informe = QAction("Imprimir informe", self)
		
		self.actionAdministrar_usuarios = QAction("Administrar usuarios",self)
		
		self.actionSalir = QAction("Salir", self)
		
		self.actionVer_lista_propietario = QAction("Ver lista",self)
		
		self.actionCrear_propietario = QAction("Crear propietario",self)
		self.actionCrear_propietario.triggered.connect(self.new_propietario)
		
		self.actionEditar = QAction("Editar",self)
		self.actionEditar.triggered.connect(self.editar_propietario)
		
		self.actionDar_de_baja = QAction("Dar de baja", self)
  
		self.actionBuscar_propietario = QAction("Buscar", self)
		
		self.actionVer_stock = QAction("Ver stock",self)
		
		self.actioninventario = QAction("Inventario",self)
		
		self.actionAnadir_producto = QAction("Añadir producto",self)
		
		self.actionDar_de_baja_almacen = QAction("Dar de baja",self)
		
		self.actionVer_lista_de_servicios = QAction("Ver lista de servicios",self)
		
		self.actionModificar_servicio = QAction("Modificar servicio",self)
		
		self.actionanadir_servicio = QAction("Añadir servicio",self)
		
		self.actionQuitar_servicio = QAction("Quitar servicio",self)
		
		self.actionVer_completo = QAction("Ver completo",self)
		
		self.actionTareas_del_dia = QAction("Tareas del dia",self)
		
		self.actionRecordatorios = QAction("Recordatorios",self)
		
		self.centralwidget = QWidget(self)
		
		
		

		self.lista_pendientes = QListView(self.centralwidget)
		self.lista_pendientes.setGeometry(QRect(50, 90, 256, 192))

		self.label_pendientes = QLabel("Pendientes:",self.centralwidget)
		self.label_pendientes.setGeometry(QRect(50, 50, 131, 17))

		self.label_citas_programadas = QLabel("Citas programadas:",self.centralwidget)
		self.label_citas_programadas.setGeometry(QRect(50, 310, 131, 17))
		self.label_recordatorios = QLabel("Recordatorios",self.centralwidget)
		self.label_recordatorios.setGeometry(QRect(350, 310, 101, 17))
		self.lista_citas_programadas = QListWidget(self.centralwidget)
		self.lista_citas_programadas.setGeometry(QRect(50, 350, 256, 192))
		self.lista_recordatorios = QListWidget(self.centralwidget)
		self.lista_recordatorios.setGeometry(QRect(350, 350, 256, 192))
		self.calendarWidget = QCalendarWidget(self.centralwidget)
		self.calendarWidget.setGeometry(QRect(330, 90, 456, 171))
		self.setCentralWidget(self.centralwidget)
		self.menubar = QMenuBar(self)
		
		self.menubar.setGeometry(QRect(0, 0, 800, 22))
		self.menuMenu = QMenu("Menú",self.menubar)
		
		self.menuPropietarios = QMenu("Propietarios", self.menubar)
		
		self.menuAlmacen = QMenu("Almacen", self.menubar)
		
		self.menuServicios = QMenu("Servicios",self.menubar)

		self.menuCalendario = QMenu("Calendario",self.menubar)
		
		self.setMenuBar(self.menubar)
		self.statusbar = QStatusBar(self)
		
		self.setStatusBar(self.statusbar)
		self.menubar.addAction(self.menuMenu.menuAction())
		self.menubar.addAction(self.menuPropietarios.menuAction())
		self.menubar.addAction(self.menuAlmacen.menuAction())
		self.menubar.addAction(self.menuServicios.menuAction())
		self.menubar.addAction(self.menuCalendario.menuAction())
		self.menuMenu.addAction(self.actionActualizar_informacion)
		self.menuMenu.addAction(self.actionImprimir_informe)
		self.menuMenu.addAction(self.actionAdministrar_usuarios)
		self.menuMenu.addAction(self.actionSalir)
		self.menuPropietarios.addAction(self.actionVer_lista_propietario)
		self.menuPropietarios.addAction(self.actionCrear_propietario)
		self.menuPropietarios.addAction(self.actionEditar)
		self.menuPropietarios.addAction(self.actionDar_de_baja)
		self.menuPropietarios.addAction(self.actionBuscar_propietario)
		self.actionBuscar_propietario.triggered.connect(self.buscar_propietario)
		
		self.menuAlmacen.addAction(self.actionVer_stock)
		self.menuAlmacen.addAction(self.actioninventario)
		self.menuAlmacen.addAction(self.actionAnadir_producto)
		self.menuAlmacen.addAction(self.actionDar_de_baja_almacen)
		self.menuServicios.addAction(self.actionVer_lista_de_servicios)
		self.menuServicios.addAction(self.actionModificar_servicio)
		self.menuServicios.addAction(self.actionanadir_servicio)
		self.menuServicios.addAction(self.actionQuitar_servicio)
		self.menuCalendario.addAction(self.actionVer_completo)
		self.menuCalendario.addAction(self.actionTareas_del_dia)
		self.menuCalendario.addAction(self.actionRecordatorios)


	def new_propietario(self):
		self.setDisabled(True)
		nuevo_propietario_view = Propietario_view(self)
		

	def editar_propietario(self):
		self.setDisabled(True)
  
	def buscar_propietario(self):
		self.setDisabled(True)
		self.ventanaBuscador = Busqueda_view(self)
		
		
		
		



if __name__ == '__main__':
	app = QApplication(sys.argv)
	test = Main_view()
	test.show()
	sys.exit(app.exec())


