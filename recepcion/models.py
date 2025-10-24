
from django.db import models

class equipo(models.Model):
    nombre = models.CharField(max_length=100)
    problema = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} ({self.problema})"

class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
