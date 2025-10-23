from django.db import models

# Create your models here.
class equipo(models.Model):
    nombre = models.CharField(max_length=100)
    problema = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE, related_name="equipos")

    def __str__(self):
        return self.nombre
