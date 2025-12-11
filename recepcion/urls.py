from django.urls import path
from .views import registrar_equipo, listado_equipos, detalle_equipo, editar_equipo, eliminar_equipo
from .api_views import api_lista_equipo, api_agregar_equipo

urlpatterns = [
    path('registrar/', registrar_equipo, name='registrar_equipo'),
    path('listado/', listado_equipos, name='listado_equipos'),
    path('detalle/<int:id>/', detalle_equipo, name='detalle_equipo'),
    path('editar/<int:id>/', editar_equipo, name='editar_equipo'),
    path('eliminar/<int:id>/', eliminar_equipo, name='eliminar_equipo'),
    path('api/equipo/', api_lista_equipo, name='api_lista_equipo'),
    path('api/equipo/agregar/', api_agregar_equipo, name='api_agregar_equipo'),
]
