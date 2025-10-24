from django.db import models
from recepcion.models import Equipo
from diagnostico.models import Diagnostico

class Entrega(models.Model):
    ESTADO_CHOICES = [
        ('NO_ENTREGADO', 'No entregado'),
        ('ENTREGADO', 'Entregado'),
    ]

    diagnostico = models.OneToOneField(Diagnostico, on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='NO_ENTREGADO',
        verbose_name='Estado de entrega'
    )

    def __str__(self):
        return f"Entrega de {self.diagnostico} - {self.get_estado_display()}"
