from django.urls import path
from .views import registrar_equipo, listado_equipos, detalle_equipo

urlpatterns = [
    path('recepcion/registrar/', registrar_equipo, name='registrar_equipo'),
    path('recepcion/listado/', listado_equipos, name='listado_equipos'),
    path('recepcion/detalle/<str:nombre>/', detalle_equipo, name='detalle_equipo'),
]