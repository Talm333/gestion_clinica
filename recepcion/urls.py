from django.urls import path
from .views import registrar_equipo, listado_equipos, detalle_equipo

urlpatterns = [
<<<<<<< HEAD
    path('recepcion/registrar/', registrar_equipo, name='registrar_equipo'),
    path('recepcion/listado/', listado_equipos, name='listado_equipos'),
    path('recepcion/detalle/<str:nombre>/', detalle_equipo, name='detalle_equipo'),
=======
    path('registrar/', registrar_equipo, name='registrar_equipo'),
    path('listado/', listado_equipos, name='listado_equipos'),
    path('detalle/<str:nombre>/', detalle_equipo, name='detalle_equipo'),
>>>>>>> e99703f12acfebac4082134a4372a8fcc356d997
]