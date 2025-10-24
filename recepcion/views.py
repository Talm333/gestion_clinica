from django.shortcuts import render, redirect
from django.contrib import messages
from .models import equipo

def registrar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    usuario = request.session.get('username', 'Invitado')
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        problema = request.POST.get('problema')
        equipo.objects.create(nombre=nombre, problema=problema)
        #message.success es para mostrar un mensaje de exito
        messages.success(request, f'Equipo de {nombre} registrado correctamente.')
        return redirect('/recepcion/listado/')
    return render(request, 'recepcion/registrar.html', {'usuario': usuario})

def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    usuario = request.session.get('username', 'Invitado')
    equipos = equipo.objects.all()
    return render(request, 'recepcion/listado.html', {'equipos': equipos, 'usuario': usuario})

def detalle_equipo(request, nombre):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    usuario = request.session.get('username', 'Invitado')
    #revisa cada equipo en la lista y encuentra el que coincide con el nombre
    equipo_obj = equipo.objects.filter(nombre=nombre).first()
    return render(request, 'recepcion/detalle.html', {'equipo': equipo_obj, 'usuario': usuario})
