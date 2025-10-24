from django.db import models
from recepcion.models import Equipo

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Diagnostico(models.Model):

    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE, related_name="diagnosticos")
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    diagnostico = models.TextField()
    solucion = models.TextField()
    TIPO_SOLUCION_CHOICES = [
        ('correctiva', 'Correctiva'),
        ('preventiva', 'Preventiva'),
    ]
    tipo_solucion = models.CharField(max_length=100, choices=TIPO_SOLUCION_CHOICES)

    def __str__(self):
        return f"Diagnóstico para {self.equipo.cliente}"
