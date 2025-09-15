diagnosticos = []
from django.shortcuts import render, redirect
diagnosticos = []
ASIGNACIONES = []
ESTUDIANTES = []
from recepcion.views import EQUIPOS

def asignar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login')
    mensaje = ''
    equipos_disponibles = [e for e in EQUIPOS if e['nombre'] not in [a['equipo'] for a in ASIGNACIONES]]
    if request.method == 'POST':
        estudiante = request.POST.get('estudiante')
        equipo = request.POST.get('equipo')
        nuevo_estudiante = request.POST.get('nuevo_estudiante')
        if nuevo_estudiante and nuevo_estudiante not in ESTUDIANTES:
            ESTUDIANTES.append(nuevo_estudiante)
            estudiante = nuevo_estudiante
        if estudiante and equipo:
            ASIGNACIONES.append({'estudiante': estudiante, 'equipo': equipo})
            mensaje = 'Asignación realizada correctamente.'
            return redirect('evaluar_equipo')
    return render(request, 'diagnostico/asignar.html', {
        'equipos': equipos_disponibles,
        'estudiantes': ESTUDIANTES,
        'mensaje': mensaje
    })

def evaluar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login')
    equipos_asignados = [a['equipo'] for a in ASIGNACIONES]
    if request.method == 'POST':
        estudiante = request.POST.get('estudiante')
        equipo = request.POST.get('equipo')
        diagnostico = request.POST.get('diagnostico')
        solucion = request.POST.get('solucion')
        tipo_solucion = request.POST.get('tipo_solucion')
        if estudiante and equipo and diagnostico and solucion and tipo_solucion:
            diagnosticos.append({
                'estudiante': estudiante,
                'equipo': equipo,
                'diagnostico': diagnostico,
                'solucion': solucion,
                'tipo_solucion': tipo_solucion,
            })
            return redirect('listado_diagnosticos')
    return render(request, 'diagnostico/evaluar.html', {
        'equipos': equipos_asignados,
        'estudiantes': ESTUDIANTES
    })

def listado_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('login')
    return render(request, 'diagnostico/diagnostico_listado.html', {'diagnosticos': diagnosticos})
