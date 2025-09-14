from django.shortcuts import render, redirect
from django.contrib import messages

# creamos una lista global para almacenar los equipos registrados
EQUIPOS = []

def registrar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    usuario = request.session.get('username', 'Invitado')
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        problema = request.POST.get('problema')
        equipo = {'nombre': nombre, 'tipo': tipo, 'problema': problema}
        EQUIPOS.append(equipo)
        #message.success es para mostrar un mensaje de exito
        messages.success(request, f'Equipo de {nombre} registrado correctamente.')
        return redirect('/recepcion/listado/')
    return render(request, 'recepcion/registrar.html', {'usuario': usuario})

def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    usuario = request.session.get('username', 'Invitado')
    return render(request, 'recepcion/listado.html', {'equipos': EQUIPOS, 'usuario': usuario})

def detalle_equipo(request, nombre):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    usuario = request.session.get('username', 'Invitado')
    #revisa cada equipo en la lista y encuentra el que coincide con el nombre
    equipo = next((e for e in EQUIPOS if e['nombre'] == nombre), None)
    return render(request, 'recepcion/detalle.html', {'equipo': equipo, 'usuario': usuario})