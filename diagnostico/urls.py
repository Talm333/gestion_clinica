from django.urls import path
from .views import diagnostico, asignar, evaluar, listado

urlpatterns = [
    path('', diagnostico, name='diagnostico'),
    path('asignar/', asignar, name='asignar_diagnostico'),
    path('evaluar/', evaluar, name='evaluar_diagnostico'),
    path('listado/', listado, name='listado_diagnostico'),
]
