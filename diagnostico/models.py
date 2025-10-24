from django.db import models
from recepcion.models import equipo

from recepcion.models import equipo


class Diagnostico(models.Model):
    
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE, related_name="diagnosticos")
    estudiante = models.CharField(max_length=100)
    diagnostico = models.TextField()
    solucion = models.TextField()
    tipo_solucion = models.CharField(max_length=100)

    def __str__(self):
        return f"Diagnóstico para {self.equipo.nombre}"
