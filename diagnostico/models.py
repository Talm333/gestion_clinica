from django.db import models
from recepcion.models import equipo

# Create your models here.
class Diagnostico(models.Model):
    estudiante = models.CharField(max_length=100)
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE, related_name="diagnosticos")
    diagnostico = models.TextField()
    solucion = models.TextField()
    tipo_solucion = models.CharField(max_length=100)

    def __str__(self):
        return f"Diagnóstico de {self.equipo.nombre} por {self.estudiante}"
