from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Equipo

def registrar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    usuario = request.session.get('username', 'Invitado')
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        tipo = request.POST.get('tipo')
        problema = request.POST.get('problema')
        Equipo.objects.create(cliente=cliente, tipo=tipo, problema=problema)
        #message.success es para mostrar un mensaje de exito
        messages.success(request, f'Equipo de {cliente} registrado correctamente.')
        return redirect('/recepcion/listado/')
    return render(request, 'recepcion/registrar.html', {'usuario': usuario})

def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    usuario = request.session.get('username', 'Invitado')
    equipos = Equipo.objects.all()
    return render(request, 'recepcion/listado.html', {'equipos': equipos, 'usuario': usuario})

def detalle_equipo(request, cliente):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    usuario = request.session.get('username', 'Invitado')
    #revisa cada equipo en la lista y encuentra el que coincide con el cliente
    equipo_obj = Equipo.objects.filter(cliente=cliente).first()
    return render(request, 'recepcion/detalle.html', {'equipo': equipo_obj, 'usuario': usuario})
