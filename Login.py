from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from Autenticator import Autenticator
from main_view import Main_view
import sys


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initiateUI()
        self.generateForm()
        self.show()
        
        
    def initiateUI(self):
        self.setFixedSize(250,400)
        self.setWindowTitle("Zoof-vet 0.01")
        self.centralwidget = QWidget(self)
        self.centralwidget.setGeometry(QRect(0, 0, 250, 400))
        
    def generateForm(self):
        self.label_user = QLabel("Usuario:",self.centralwidget)
        self.edit_user = QLineEdit(self.centralwidget)
        
        self.form = QFormLayout(self.centralwidget)
        self.form.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.form.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_user)
        self.form.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_user)
                
        self.password_label = QLabel("Contraseña:", self.centralwidget)
        self.password_edit = QLineEdit(self.centralwidget)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.form.setWidget(1, QFormLayout.ItemRole.LabelRole, self.password_label)
        self.form.setWidget(1, QFormLayout.ItemRole.FieldRole, self.password_edit)
    
        self.buton_cancel = QPushButton("Cancelar", self.centralwidget)
        self.buton_cancel.clicked.connect(self.Close)
        self.buton_login = QPushButton("Entrar", self.centralwidget)
        self.form.setWidget(2, QFormLayout.ItemRole.LabelRole, self.buton_cancel)
        self.form.setWidget(2, QFormLayout.ItemRole.FieldRole, self.buton_login)
        
        self.buton_login.clicked.connect(self.login)

        
    def login(self):
        autenticatorObject = Autenticator(self, self.edit_user.text(),self.password_edit.text())
        autenticatorObject.autenticate()
        if autenticatorObject.isAutenticated():
            self.main = Main_view()
            self.close()
        else: 
            self.setDisabled(True)
            self.warning(self, "No has podido iniciar sesión")
            
    def warning(self, error):
        self.setDisabled(True)
        print(error)
        self.warning = Warning(self, error)
        
    def Close(self):
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Login()
    test.show()
    sys.exit(app.exec())

    