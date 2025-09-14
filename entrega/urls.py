from django.urls import path
from .views import verificar, reporte, comprobante

urlpatterns = [
    path('verificar/', verificar, name='verificar_entrega'),
    path('reporte/', reporte, name='reporte_entrega'),
    path('comprobante/', comprobante, name='comprobante_entrega'),
]