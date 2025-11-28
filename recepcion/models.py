from django.db import models

class Equipo(models.Model):
    # no es unico para que pueda haber mas de un equipo con el mismo nombre de cliente
    cliente = models.CharField(max_length=100, verbose_name='Nombre del cliente')
    tipo = models.CharField(max_length=50, verbose_name='Tipo de equipo')
    problema = models.TextField(verbose_name='Descripción del problema')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de recepción')

    def __str__(self):
        return f"#{self.id} {self.cliente} - {self.tipo}"
