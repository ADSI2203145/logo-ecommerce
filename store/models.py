from django.db import models
from django.contrib.auth.models import User






class Rol(models.Model):

	nombre_rol = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.nombre_rol
 
class Ciudad(models.Model):
	codigo = models.IntegerField(unique=True) 
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return str(self.id) + ' ' + self.nombre + ' ' + str(self.codigo)

class Persona(models.Model):
	cedula          = models.IntegerField(unique=True)
	nombre          = models.CharField(max_length=50)
	apellidos       = models.CharField(max_length=50)
	telefono        = models.CharField(max_length=15, null= True, blank = True)
	direccion       = models.CharField(max_length=100, null= True, blank = True)
	rol             = models.ForeignKey(Rol, on_delete=models.CASCADE)
	ciudad          = models.ForeignKey(Ciudad, on_delete=models.CASCADE) 
	user 			= models.OneToOneField(User, on_delete=models.CASCADE) 
	# Uno a Uno entre User y Persona, un User Solo tendra una persona asociada

	def __str__(self):
		return self.nombre + ' ' + self.apellidos 

class Categoria (models.Model):
	codigo 				= models.IntegerField(unique=True)
	nombre 				= models.CharField(max_length=50)
	especificaciones 	= models.TextField(max_length=500, null= True, blank = True)  

	def __str__(self):
		return self.nombre 

class Producto (models.Model):
	codigo 				= models.IntegerField(unique=True)
	nombre 				= models.CharField(max_length=30, unique=True)
	precio 				= models.DecimalField(max_digits = 8, decimal_places = 2)
	fecha_vencimiento 	= models.DateField( null= True, blank = True)
	especificaciones 	= models.TextField(max_length = 5000, null= True, blank = True)
	peso 				= models.CharField(max_length = 5, null= True, blank = True) # 10kg
	foto 				= models.ImageField(upload_to = 'productos', null= True, blank = True) # 10kg
	categoria 			= models.ForeignKey(Categoria, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre 

class Factura (models.Model):
	nombre_entidad 		= models.CharField(max_length=30, unique=True, default='Ecommerce Santander')
	fecha_compra 		= models.DateTimeField(auto_now_add = True)
	total 				= models.FloatField(default = 0) 
	iva 				= models.IntegerField()  
	direccion       	= models.CharField(max_length=100)
	cliente				= models.ForeignKey(Persona, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.cliente.cedula) + self.cliente.nombre + ' ' + str(self.id)


class Detalle (models.Model):
	cantidad = models.IntegerField()
	subtotal = models.IntegerField()
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	fatura   = models.ForeignKey(Factura, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.factura.id)+ ' ' + str(self.producto.nombre) + str(self.cantidad) + ' ' + str(self.id)










