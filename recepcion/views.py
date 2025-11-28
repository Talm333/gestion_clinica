from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Equipo
from .forms import EquipoForm

def registrar_equipo(request):
    # verifica si el usuario esta autenticado
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    
    usuario = request.session.get('username', 'Invitado')

    #crea un formulario
    form = EquipoForm()
    #si el metodo es post, se guarda el formulario
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            #message.success es para mostrar un mensaje de exito
            messages.success(request, 'Equipo registrado correctamente.')
            return redirect('/recepcion/listado/')
    return render(request, 'recepcion/registrar.html', {'usuario': usuario, 'form': form})

def listado_equipos(request):
    #verifica si el usuario esta autenticado
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    #obtiene todos los equipos
    equipos = Equipo.objects.all()
    return render(request, 'recepcion/listado.html', {'equipos': equipos, 'usuario': request.session.get('username', 'Invitado')})

def detalle_equipo(request, id):
    #verifica si el usuario esta autenticado
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    #revisa cada equipo en la lista y encuentra el que coincide con el id del equipo
    equipo_obj = Equipo.objects.get(id=id)
    return render(request, 'recepcion/detalle.html', {'equipo': equipo_obj, 'usuario': request.session.get('username', 'Invitado')})

def editar_equipo(request, id):
    #verifica si el usuario esta autenticado
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    #obtiene el equipo que coincide con el id
    equipo = Equipo.objects.get(id=id)
    #crea un formulario con el equipo se pasa instance para que el formulario tenga los datos del equipo
    form = EquipoForm(instance=equipo)
    #si el metodo es post, se guarda el formulario
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipo actualizado correctamente.')
            return redirect('listado_equipos')
    return render(request, 'recepcion/editar.html', {'form': form, 'usuario': request.session.get('username', 'Invitado'), 'equipo': equipo})

def eliminar_equipo(request, id):
    #verifica si el usuario esta autenticado
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    #obtiene el equipo que coincide con el id
    equipo = Equipo.objects.get(id=id)
    #si el metodo es post, se elimina el equipo
    if request.method == 'POST':
        equipo.delete()
        messages.success(request, 'Equipo eliminado correctamente.')
        return redirect('listado_equipos')
    return render(request, 'recepcion/eliminar.html', {'equipo': equipo, 'usuario': request.session.get('username', 'Invitado')})
