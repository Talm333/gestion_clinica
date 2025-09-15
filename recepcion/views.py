from django.shortcuts import render, redirect
from django.contrib import messages
<<<<<<< HEAD
EQUIPOS = []
from diagnostico.views import ASIGNACIONES
from entrega.views import ESTADOS_ENTREGA

def registrar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login')
=======

# creamos una lista global para almacenar los equipos registrados
EQUIPOS = []

def registrar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
>>>>>>> e99703f12acfebac4082134a4372a8fcc356d997
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
<<<<<<< HEAD
        return redirect('login')
    usuario = request.session.get('username', 'Invitado')
    asignados = {a['equipo']: a['estudiante'] for a in ASIGNACIONES}
    equipos_con_asignado = []
    for equipo in EQUIPOS:
        estudiante_asignado = asignados.get(equipo['nombre'])
        estado = ESTADOS_ENTREGA.get(equipo['nombre'])
        estado_entrega = estado.get('estado_entrega', 'Pendiente') if estado else 'Pendiente'
        equipos_con_asignado.append({
            'nombre': equipo['nombre'],
            'tipo': equipo['tipo'],
            'problema': equipo['problema'],
            'estudiante_asignado': estudiante_asignado,
            'estado_entrega': estado_entrega
        })
    return render(request, 'recepcion/listado.html', {'equipos': equipos_con_asignado, 'usuario': usuario})

def detalle_equipo(request, nombre):
    if not request.session.get('autenticado'):
        return redirect('login')
    usuario = request.session.get('username', 'Invitado')
    #revisa cada equipo en la lista y encuentra el que coincide con el nombre
    equipo = next((e for e in EQUIPOS if e['nombre'] == nombre), None)
    # Buscar si el equipo está asignado a algún estudiante
    estudiante_asignado = None
    for a in ASIGNACIONES:
        if a['equipo'] == nombre:
            estudiante_asignado = a['estudiante']
            break
    return render(request, 'recepcion/detalle.html', {'equipo': equipo, 'usuario': usuario, 'estudiante_asignado': estudiante_asignado})
=======
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
>>>>>>> e99703f12acfebac4082134a4372a8fcc356d997
