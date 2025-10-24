from django.db import models
from recepcion.models import Equipo

from diagnostico.models import Diagnostico

class Entrega(models.Model):

    diagnostico = models.OneToOneField(Diagnostico, on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f"Entrega de {self.diagnostico}"
