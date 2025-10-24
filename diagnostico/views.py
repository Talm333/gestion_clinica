from django.shortcuts import render, redirect
from .models import Diagnostico, Estudiante
from recepcion.models import Equipo

def asignar_equipo(request):
    estudiantes = Estudiante.objects.all()
    if request.method == 'POST':
        estudiante = request.POST.get('estudiante')
        equipo_id = request.POST.get('equipo')
        # Aquí podrías guardar la asignación si lo necesitas
        return redirect('evaluar_equipo')
    return render(request, 'diagnostico/asignar.html', {'estudiantes': estudiantes})

def evaluar_equipo(request):
    estudiantes = Estudiante.objects.all()
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante')
        equipo_id = request.POST.get('equipo')
        diagnostico_text = request.POST.get('diagnostico')
        solucion = request.POST.get('solucion')
        tipo_solucion = request.POST.get('tipo_solucion')
        equipo_obj = Equipo.objects.get(id=equipo_id)
        estudiante_obj = Estudiante.objects.get(id=estudiante_id)
        Diagnostico.objects.create(
            estudiante=estudiante_obj,
            equipo=equipo_obj,
            diagnostico=diagnostico_text,
            solucion=solucion,
            tipo_solucion=tipo_solucion
        )
        return redirect('listado_diagnosticos')
    return render(request, 'diagnostico/evaluar.html', {'estudiantes': estudiantes})

def listado_diagnosticos(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'diagnostico/diagnostico_listado.html', {'diagnosticos': diagnosticos})
