from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre del estudiante')

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    equipo = models.OneToOneField('recepcion.Equipo', on_delete=models.CASCADE, related_name="asignacion")
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f"Asignación: {self.equipo} -> {self.estudiante}"

class Diagnostico(models.Model):

    equipo = models.OneToOneField('recepcion.Equipo', on_delete=models.CASCADE, related_name="diagnosticos")
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    diagnostico = models.TextField()
    solucion = models.TextField()
    TIPO_SOLUCION_CHOICES = [
        ('correctiva', 'Correctiva'),
        ('preventiva', 'Preventiva'),
    ]
    tipo_solucion = models.CharField(max_length=100, choices=TIPO_SOLUCION_CHOICES)

    def __str__(self):
        return f"Diagnóstico para {self.equipo.cliente} - {self.tipo_solucion}"

    

