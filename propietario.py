
class Propietario():

	def __init__(self, propietario):
		self.id = propietario[0]
		self.name = propietario[1]
		self.telefono = propietario[2]
		self.direccion = propietario[3]
		
	def get_name(self):
		return self.name 

	def set_name(self, new_name):
		self.name = new_name

	def add_pago(self, pago):
		self.deuda = self.deuda+pago

	def add_deuda(self, deuda):
		self.deuda = self.deuda+deuda
  
	def get_deuda(self):
		return self.deuda

	def add_mascota(self, new_mascota):
		self.mascotas.append(new_mascota)
  
	def get_telefono(self):
		return self.telefono
  
	def set_telefono(self, telefono):
		self.telefono = telefono

	def get_mascotas(self):
		return self.mascotas

	def del_mascota(self, mascota):
		self.mascotas.remove(mascota)

	def set_direccion(self, direccion):
		self.direccion = direccion
  
	def get_direccion(self):
		return self.direccion

	