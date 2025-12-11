from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Equipo
from .serializers import EquipoSerializer
from rest_framework import status

@api_view(['GET'])
def api_lista_equipo(request):
    equipo = Equipo.objects.all()
    serializer = EquipoSerializer(equipo, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def api_agregar_equipo(request):
    serializer = EquipoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)