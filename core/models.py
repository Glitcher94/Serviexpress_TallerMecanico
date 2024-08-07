from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE
from .validators import validar, validar2, validar3



# Create your models here.

class Categoria(models.Model):

    idCategoria = models.IntegerField(primary_key=True)

    nombreCategoria = models.CharField(max_length=50)

    def _str_(self):

        return self.idCategoria

    def __str__(self):
        return self.nombreCategoria

class RegistroCliente(models.Model):

    correo=models.CharField(max_length=20, primary_key=True)

    nombre=models.CharField(max_length=40)
    
    rut=models.CharField(max_length=10)

    fecha_nacimiento=models.CharField(max_length=40)

    direccion=models.CharField(max_length=40)

    estado_civil=models.CharField(max_length=10)

    contrasena = models.CharField(max_length=10, )

    confirmar_contrasena = models.CharField(max_length=10)


    def _str_(self):

        return self.correo

    def __str__(self):

        return self.correo

class RegistroAdministrador(models.Model):

    correo=models.CharField(max_length=20, primary_key=True)

    nombre=models.CharField(max_length=40)

    rut=models.CharField(max_length=40)

    fecha_nacimiento=models.CharField(max_length=40)

    direccion=models.CharField(max_length=40)

    estado_civil=models.CharField(max_length=10)

    contrasena = models.CharField(max_length=10)

    def _str_(self):

        return self.correo

class RegistroEmpleado(models.Model):

    correo=models.CharField(max_length=20, primary_key=True)

    nombre=models.CharField(max_length=40)

    rut=models.CharField(max_length=40)

    fecha_nacimiento=models.CharField(max_length=40)

    direccion=models.CharField(max_length=40)
    
    estado_civil=models.CharField(max_length=10)

    contrasena = models.CharField(max_length=10)

    confirmar_contrasena = models.CharField(max_length=10)

    def _str_(self):

        return self.correo

class Articulo(models.Model):

    idArticulo=models.CharField(max_length=20, primary_key=True)

    nombre=models.CharField(max_length=40)

    precio=models.IntegerField()

    cantidad=models.IntegerField()
    
    foto = models.TextField(max_length=290)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def _str_(self):

        return self.idArticulo

class RegistroHora(models.Model):

    idRegistro=models.CharField(max_length=20, primary_key=True)

    hora=models.CharField(max_length=10)

    dia=models.CharField(max_length=10)

    modelo=models.CharField(max_length=10)

    anno=models.CharField(max_length=10)

    descripcion=models.CharField(max_length=100)

    def _str_(self):

        return self.idRegistro

class RegistroHoraEmpleado(models.Model):

    idRegistro=models.CharField(max_length=20, primary_key=True)

    hora=models.CharField(max_length=10)

    dia=models.CharField(max_length=10)

    modelo=models.CharField(max_length=10)

    anno=models.CharField(max_length=10)

    descripcion=models.CharField(max_length=100)

    cliente = models.ForeignKey(RegistroCliente, on_delete=models.CASCADE)

    def _str_(self):

        return self.idRegistro

class RegistroProveedor(models.Model):

    codigoProveedor=models.CharField(max_length=20, primary_key=True)

    nombre=models.CharField(max_length=10)

    rut=models.CharField(max_length=10)

    direccion=models.CharField(max_length=40)

    telefono=models.CharField(max_length=10)

    giro=models.CharField(max_length=10)

    correo=models.CharField(max_length=20)

    def _str_(self):

        return self.codigoProveedor

class RegistroServicio(models.Model):

    codigo_servicio=models.CharField(max_length=20, primary_key=True)

    nombre_servicio=models.CharField(max_length=10)

    precio=models.IntegerField()

    observacion=models.CharField(max_length=200)

    def _str_(self):

        return self.codigo_servicio

