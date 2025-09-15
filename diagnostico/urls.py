from django.urls import path
from . import views

urlpatterns = [
    path('diagnostico/asignar/', views.asignar_equipo, name='asignar_equipo'),
    path('diagnostico/evaluar/', views.evaluar_equipo, name='evaluar_equipo'),
    path('diagnostico/listado/', views.listado_diagnosticos, name='listado_diagnosticos'),
]
