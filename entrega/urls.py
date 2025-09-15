from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('entrega/verificar/', views.verificar_equipo, name='verificar_equipo'),
    path('entrega/reporte/', views.reporte_entrega, name='reporte_entrega'),
=======
    path('verificar/', views.verificar_equipo, name='verificar_equipo'),
    path('reporte/', views.reporte_entrega, name='reporte_entrega'),
    path('comprobante/', views.comprobante_entrega, name='comprobante_entrega'),
>>>>>>> e99703f12acfebac4082134a4372a8fcc356d997
]