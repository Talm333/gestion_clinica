from django.urls import path
from . import views

urlpatterns = [
    path('verificar/', views.verificar_equipo, name='verificar_equipo'),
    path('reporte/', views.reporte_entrega, name='reporte_entrega'),
    path('comprobante/<int:id>/', views.comprobante_entrega, name='comprobante_entrega'),
    path('listado/', views.listado_entregas, name='listado_entregas'),
]