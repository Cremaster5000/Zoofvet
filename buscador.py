import mysql.connector 

class Buscador():
    def __init__(self):
        pass   
        
    def conectar(self):
        self.conector = mysql.connector.connect(user ='root', password = 'Octubre3749', 
                                                host = '127.0.0.1',
                                                database = 'Control_veterinaria')
        return self.conector.cursor()
        
    def cerrarConexion(self):
        self.conector.close()
    
    def buscarPropietario(self,propietario):
        try:
            cursor = self.conectar()
            cursor.execute("SELECT * FROM propietarios WHERE nombre = %s",(propietario,))
            self.consulta = cursor.fetchall()
            self.cerrarConexion()
            return self.consulta
        except mysql.connector.Error as error:
            self.cerrarConexion()
                    
    def buscarMascota(self, mascota):
        try:
            cursor = self.conectar()
            cursor.execute("SELECT * FROM mascotas WHERE nombre = (%s)",(mascota,))
            self.consulta = cursor.fetchall()
            self.cerrarConexion()
            return self.consulta
        except mysql.connector.Error as error:
            self.cerrarConexion()
            
    def buscarMascotaPropietario(self, propietario):
        try:
            cursor = self.conectar()
            cursor.execute("SELECT * FROM mascotas WHERE nombre = (%s)",(mascota,))
            self.consulta = cursor.fetchall()
            self.cerrarConexion()
            return self.consulta
        except mysql.connector.Error as error:
            self.cerrarConexion()
        
    def buscarTelefono(self, telefono):
        try:
            cursor = self.conectar()
            cursor.execute("SELECT * FROM propietario WHERE telefono = %s",(telefono,))
            self.consulta = cursor.fetchall()
            self.cerrarConexion()
            return self.consulta
        except mysql.connector.Error as error:
            self.cerrarConexion()
                
    def buscarConsulta(self, consulta):
        try:
            cursor = self.conectar()
            cursor.execute("SELECT * FROM consultas WHERE id = %(consulta)s",(consulta,))
            self.consulta = cursor.fetchall()
            self.cerrarConexion()
            return self.consulta  
        except mysql.connector.Error as error:
            self.cerrarConexion()
         
    def buscarDireccion(self, direccion):
        try:
            cursor = self.conectar()
            cursor.execute("SELECT * FROM direccion WHERE id = %(direccion)s",(direccion,))
            self.consulta = cursor.fetchall()
            self.cerrarConexion()
            return self.consulta  
        except mysql.connector.Error as error:
            self.cerrarConexion()
            

             
    
    