from datetime import *



class Consulta ():
    def __init__(self,idAnimal):
        self.fecha = datetime.today()
        self.hora = datetime.now()
        self.idAnimal = idAnimal
        
        
    def setAnamnesis(self,anamnesis):
        self.anamnesis = anamnesis
        
    def setTratamiento(self,tratamiento):
        self.tratamiento = tratamiento
        
    def setFrecuencias(self, frecuencias):
        self.frecuencias = frecuencias  
        
    def getAnamnesis(self):
        return self.anamnesis
        
    def getTratamiento(self):
        return self.tratamiento
        
    def getFrecuencias(self):
        return self.frecuencias
         