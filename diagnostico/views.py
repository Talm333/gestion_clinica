from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Diagnostico
from recepcion.models import equipo

def asignar_equipo(request):
    if request.method == 'POST':
        estudiante = request.POST.get('estudiante')
        equipo_id = request.POST.get('equipo')
        # Aquí podrías guardar la asignación si lo necesitas
        return redirect('evaluar_equipo')
    return render(request, 'diagnostico/asignar.html')

def evaluar_equipo(request):
    if request.method == 'POST':
        estudiante = request.POST.get('estudiante')
        equipo_id = request.POST.get('equipo')
        diagnostico_text = request.POST.get('diagnostico')
        solucion = request.POST.get('solucion')
        tipo_solucion = request.POST.get('tipo_solucion')
        equipo_obj = equipo.objects.get(id=equipo_id)
        Diagnostico.objects.create(
            estudiante=estudiante,
            equipo=equipo_obj,
            diagnostico=diagnostico_text,
            solucion=solucion,
            tipo_solucion=tipo_solucion
        )
        return redirect('listado_diagnosticos')
    return render(request, 'diagnostico/evaluar.html')

def listado_diagnosticos(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'diagnostico/diagnostico_listado.html', {'diagnosticos': diagnosticos})
