
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys 
from buscador import Buscador
from Warning  import Warning
from propietario_view import Propietario_view
from propietario import Propietario


class Busqueda_view(QMainWindow):
    def __init__(self, parent: QMainWindow):
        super().__init__()
        self.parent = parent
        self.setupUi() 
             
        
    def setupUi(self):
        self.setWindowTitle("Busqueda")
        self.setFixedSize(800, 300)
        
        self.centralwidget = QWidget(self)
        self.botonBuscar = QPushButton("Buscar",self.centralwidget)
        self.botonBuscar.setGeometry(QRect(124, 230, 80, 25))
        self.botonBuscar.clicked.connect(self.buscar)
        self.botonCancelar = QPushButton("Cancelar",self.centralwidget)
        self.botonCancelar.setGeometry(QRect(38, 230, 80, 25))
        self.botonCancelar.clicked.connect(self.cancelar)
        
        self.botonAbrir = QPushButton("Abrir", self.centralwidget)
        self.botonAbrir.setGeometry(QRect(210, 230, 80, 25))
        self.botonAbrir.clicked.connect(self.abrirPropietario)
        self.lista_resultados = QListWidget(self.centralwidget)
        self.lista_resultados.setGeometry(QRect(330, 70, 431, 181))
        self.scrollbar = QScrollBar(self)
        self.lista_resultados.addScrollBarWidget(self.scrollbar, Qt.AlignmentFlag.AlignRight)
        self.lista_resultados.setItemAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(40, 70, 220, 128))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()

        self.label_nombre = QLabel("Nombre:", self.widget)
        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_nombre)
        self.edit_nombre = QLineEdit(self.widget)
        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_nombre)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        
        self.label_telefono = QLabel("Telefono:",self.widget)
        self.edit_telefono = QLineEdit(self.widget)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_telefono)
        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_telefono)


        self.gridLayout.addLayout(self.formLayout_2, 1, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.label_direccion = QLabel("Dirección:", self.widget)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_direccion)

        self.edit_direccion = QLineEdit(self.widget)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_direccion)


        self.gridLayout.addLayout(self.formLayout_3, 2, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.label_mascotas = QLabel("Mascotas:", self.widget)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_mascotas)

        self.edit_mascotas = QLineEdit(self.widget)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_mascotas)


        self.gridLayout.addLayout(self.formLayout_4, 3, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.show()
        
    def cancelar(self):
        self.close()
        
    def buscar(self):
        self.buscador = Buscador()
        nombre = self.edit_nombre.text()
        telefono = self.edit_telefono.text()
        direccion = self.edit_direccion.text()
        mascota = self.edit_mascotas.text()
        print("info obtenida")
        if nombre != "":
            self.info = self.buscador.buscarPropietario(nombre)
            self.displayInfo()
        elif telefono != "":
            self.info = self.buscador.buscarTelefono(telefono)
            self.displayInfo()
        elif direccion != "":
            self.info = self.buscador.buscarDireccion(direccion)
            self.displayInfo()
        elif mascota != "":
            self.info = self.buscador.buscarMascota(mascota)
            self.displayInfo()
        else: 
            print("no hay info")
            self.setDisabled(True)
            self.warning = Warning(self, "Ingrese información a buscar")     
                       
    def displayInfo(self):
        informacion = list(self.info)
        self.warning = Warning(self, informacion)
        space = "    "
        for i in informacion:
            item = informacion.pop()
            item = str(item[0])+space+item[1]+space+item[2]+space+item[3]           
            self.lista_resultados.addItem(item)
            
    def abrirPropietario(self):
        id = self.lista_resultados.currentRow()
        propietario = Propietario(self.info[id])
        self.propietarioVista = Propietario_view(self, propietario)
        
        self.setDisabled(True)
        
    def new_warning(self, info):
        self.setDisabled(True)
        self.warning = Warning(self, info)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    test = Busqueda_view("lol")
    sys.exit(app.exec())
