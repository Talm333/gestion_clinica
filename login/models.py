from django.db import models

# Create your models here.
class rol(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del rol")
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")

    def __str__(self):
        return self.nombre
   
class usuario(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    contraseña = models.CharField(max_length=100)
    rol_id = models.ForeignKey(rol, on_delete=models.CASCADE, related_name="usuarios")

    def __str__(self):
        return self.nombre