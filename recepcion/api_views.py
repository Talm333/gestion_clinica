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

@api_view(['PUT'])
def api_actualizar_equipo(request, id):
    try:
        equipo = Equipo.objects.get(id=id)
    except Equipo.DoesNotExist:
        return Response({'error': 'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EquipoSerializer(equipo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_eliminar_equipo(request, id):
    try:
        equipo = Equipo.objects.get(id=id)
    except Equipo.DoesNotExist:
        return Response({'error': 'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    equipo.delete()
    return Response({'mensaje': 'Equipo eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)