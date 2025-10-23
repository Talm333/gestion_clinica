from django.db import models
from recepcion.models import equipo

# Create your models here.
class Entrega(models.Model):
    cliente = models.CharField(max_length=100)
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE, related_name="entregas")
    diagnostico = models.TextField()
    estado_final = models.CharField(max_length=100)
    observaciones = models.TextField()

    def __str__(self):
        return f"Entrega de {self.equipo.nombre} a {self.cliente}"
