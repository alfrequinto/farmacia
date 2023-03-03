from django.db import models

# Create your models here.

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.IntegerField('Telefono',blank=True,null=False) 
    cargo = models.CharField(max_length=50)

    def __str__(self):
      texto ="{0} ({1})"
      return texto.format( self.nombres, self.apellidos,  self.telefono, self.cargo)


class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    codigo = models.IntegerField('Codigo',blank=False,null=False)
    telefono = models.IntegerField('Telefono',blank=False,null=False) 


    def __str__(self):
      texto = "{0} ({1} {2})"
      return texto.format(self.id, self.nombres, self.apellidos)


class Proveedor(models.Model):
  id = models.AutoField(primary_key=True)
  nombre_proveedor = models.CharField(max_length=50)	
  ruc = models.CharField(max_length=10)
  telefono = models.CharField(max_length=10)
  direccion = models.CharField(max_length=60)

         
class Medicamento(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=200, unique=True)
  fecha_expiracion = models.DateField()
  fecha_produccion = models.DateField()	
  precio_Compra = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
  precio_venta = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)