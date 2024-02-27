

class Mascota():
	def __init__(self, name, age, breed, sex):
		self.name = name  
		self.age = age  
		self.breed = breed  
		self.sex = sex  
		self.live = True
		self.lista_consultas = []

	def get_name(self):
		return self.name  

	def change_name(self, new_name):
		self.name = new_name

	def change_age(self, new_age):
		self.age = new_age  

	def change_breed(self, new_breed):
		self.breed = new_breed

	def defunct(self):
		self.live = False

	def change_live(self):
		self.live = True

	def add_consulta(self, consulta):
		self.lista_consultas.append(consulta)

	def del_consulta(self, consulta):
		self.lista_consultas.remove(consulta)

	def get_consultas(self):
		return self.lista_consultas

	