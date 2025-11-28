from django.shortcuts import render, redirect
from django.contrib import messages
from recepcion.models import Equipo
from .models import Diagnostico, Estudiante, Asignacion
from .forms import DiagnosticoForm, AsignacionForm, SeleccionEquipoForm

def asignar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    
    form = AsignacionForm()
    
    if request.method == 'POST':
        form = AsignacionForm(request.POST)
        if form.is_valid():
            # validamos si se ingreso un estudiante nuevo o se selecciono uno
            nuevo_nombre = request.POST.get('nuevo_estudiante')
            estudiante_seleccionado = request.POST.get('estudiante')

            if not nuevo_nombre and not estudiante_seleccionado:
                messages.error(request, "Debe seleccionar un estudiante o ingresar uno nuevo.")
                return render(request, 'diagnostico/asignar.html', {'form': form})
            
            if nuevo_nombre:
                estudiante_obj, _ = Estudiante.objects.get_or_create(nombre=nuevo_nombre)
                form.instance.estudiante = estudiante_obj
            
            form.save()
            messages.success(request, "Equipo asignado correctamente.")
            return redirect('listado_diagnosticos')
            
    return render(request, 'diagnostico/asignar.html', {'form': form})

def evaluar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    
    equipo_id = request.GET.get('equipo')
    
    # si no hay id mostramos el formulario de seleccion
    if not equipo_id:
        if request.method == 'POST':
            # obtenemos el id del equipo directamente del post
            equipo_id_seleccionado = request.POST.get('equipo')
            if equipo_id_seleccionado:
                return redirect(f'/diagnostico/evaluar/?equipo={equipo_id_seleccionado}')
        else:
            seleccion_form = SeleccionEquipoForm()
            
        return render(request, 'diagnostico/evaluar.html', {'seleccion_form': seleccion_form})
    
    # si hay id mostramos el formulario de diagnostico
    asignacion = Asignacion.objects.get(equipo__id=equipo_id)
    
    form = DiagnosticoForm()
    
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            # guardado
            form.instance.equipo = asignacion.equipo
            form.instance.estudiante = asignacion.estudiante
            form.save()
            messages.success(request, "Diagnóstico registrado correctamente.")
            return redirect('listado_diagnosticos')
            
    return render(request, 'diagnostico/evaluar.html', {'form': form, 'asignacion': asignacion})

def listado_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    
    diagnosticos = Diagnostico.objects.all()
    
    return render(request, 'diagnostico/diagnostico_listado.html', {
        'diagnosticos': diagnosticos
    })
