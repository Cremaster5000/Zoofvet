import hashlib
import mysql.connector
import datetime
import os
from dotenv import load_dotenv
from Warning import Warning



class Autenticator():
    def __init__(self,parent, USER,PASSWORD):
        self.parent  = parent
        self.log_keys = [USER, self.encript(PASSWORD)]
        self.autenticated = False
        load_dotenv()
        
    def isAutenticated(self):
        return self.autenticated
        
    def encript(self, item):
        hashed = hashlib.sha256(item.encode())
        return hashed.hexdigest()
        
    def autenticate(self):
        try:
            cursor = self.conectDB()
            cursor.execute("SELECT * FROM USUARIOS WHERE nombre=%s", (self.log_keys[0],))
            resultado = cursor.fetchall()
            print(resultado[0][2])
            print(self.log_keys[1])
            if resultado[0][2] == self.log_keys[1]: self.autenticated = True
            self.updateLastLogin(resultado[0][0])
        except Exception as error:
            self.parent.warning(str(error))
        finally:
            self.conector.close()
    
    def conectDB(self):
        self.conector = mysql.connector.connect(user =os.getenv("DB_USER"), 
                                                password = os.getenv("DB_PASSWORD"), 
                                                host = os.getenv("DB_HOST"),
                                                database = os.getenv("DATABASE"))
        return self.conector.cursor()
  
        
    def updateLastLogin(self, id):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            cursor = self.conectDB()    
            cursor.execute("UPDATE USUARIOS SET lastlog=%s WHERE id=%s", (now, id))
            self.conector.commit()
        except Exception as error:
            self.parent.warning(str(error))
        finally:
            self.conector.close()
        