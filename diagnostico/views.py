from django.shortcuts import render, redirect
from django.http import HttpResponse

# Simulación de datos en memoria
diagnosticos = []

def asignar_equipo(request):
    if request.method == 'POST':
        estudiante = request.POST.get('estudiante')
        equipo = request.POST.get('equipo')
        # Aquí podrías guardar la asignación si lo necesitas
        return redirect('evaluar_equipo')
    return render(request, 'diagnostico/asignar.html')

def evaluar_equipo(request):
    if request.method == 'POST':
        estudiante = request.POST.get('estudiante')
        equipo = request.POST.get('equipo')
        diagnostico = request.POST.get('diagnostico')
        solucion = request.POST.get('solucion')
        tipo_solucion = request.POST.get('tipo_solucion')
        diagnosticos.append({
            'estudiante': estudiante,
            'equipo': equipo,
            'diagnostico': diagnostico,
            'solucion': solucion,
            'tipo_solucion': tipo_solucion,
        })
        return redirect('listado_diagnosticos')
    return render(request, 'diagnostico/evaluar.html')

def listado_diagnosticos(request):
    return render(request, 'diagnostico/diagnostico_listado.html', {'diagnosticos': diagnosticos})
