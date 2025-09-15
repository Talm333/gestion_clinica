from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('diagnostico/asignar/', views.asignar_equipo, name='asignar_equipo'),
    path('diagnostico/evaluar/', views.evaluar_equipo, name='evaluar_equipo'),
    path('diagnostico/listado/', views.listado_diagnosticos, name='listado_diagnosticos'),
=======
    path('asignar/', views.asignar_equipo, name='asignar_equipo'),
    path('evaluar/', views.evaluar_equipo, name='evaluar_equipo'),
    path('listado/', views.listado_diagnosticos, name='listado_diagnosticos'),
>>>>>>> e99703f12acfebac4082134a4372a8fcc356d997
]
