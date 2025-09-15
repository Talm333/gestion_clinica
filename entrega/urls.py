from django.urls import path
from . import views

urlpatterns = [
    path('entrega/verificar/', views.verificar_equipo, name='verificar_equipo'),
    path('entrega/reporte/', views.reporte_entrega, name='reporte_entrega'),
]