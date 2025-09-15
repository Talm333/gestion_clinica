<<<<<<< HEAD

from django.shortcuts import render, redirect
equipos_entregados = []
from recepcion.views import EQUIPOS
ESTADOS_ENTREGA = {}

def verificar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login')
=======
from django.shortcuts import render, redirect

# Simulación de datos en memoria
equipos_entregados = []

def verificar_equipo(request):
>>>>>>> e99703f12acfebac4082134a4372a8fcc356d997
    estado = None
    cliente = ''
    if request.method == 'GET' and 'cliente' in request.GET:
        cliente = request.GET.get('cliente')
        equipo = next((e for e in equipos_entregados if e['cliente'] == cliente), None)
        if equipo:
            estado = equipo
        else:
<<<<<<< HEAD
            equipo_registrado = next((e for e in EQUIPOS if e['nombre'] == cliente), None)
            if equipo_registrado:
                try:
                    from diagnostico.views import diagnosticos
                except ImportError:
                    diagnosticos = []
                diag = next((d for d in diagnosticos if d['equipo'] == cliente), None)
                estado = {
                    'cliente': equipo_registrado['nombre'],
                    'equipo': equipo_registrado['tipo'],
                    'diagnostico': diag['diagnostico'] if diag else 'Sin diagnóstico',
                    'estado_final': 'Pendiente',
                    'observaciones': equipo_registrado.get('problema', '')
                }
            else:
                estado = 'No encontrado'
    # ...existing code...
    clientes_registrados = [e['nombre'] for e in EQUIPOS]
    return render(request, 'entrega/verificar.html', {'estado': estado, 'cliente': cliente, 'clientes': clientes_registrados})

def reporte_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('login')
    clientes_registrados = [e['nombre'] for e in EQUIPOS]
    equipos_registrados = [e['nombre'] for e in EQUIPOS]
=======
            estado = 'No encontrado'
    return render(request, 'entrega/verificar.html', {'estado': estado, 'cliente': cliente})

def reporte_entrega(request):
    mensaje = ''
>>>>>>> e99703f12acfebac4082134a4372a8fcc356d997
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        equipo = request.POST.get('equipo')
        diagnostico = request.POST.get('diagnostico')
        estado_final = request.POST.get('estado_final')
        observaciones = request.POST.get('observaciones')
        equipos_entregados.append({
            'cliente': cliente,
            'equipo': equipo,
            'diagnostico': diagnostico,
            'estado_final': estado_final,
            'observaciones': observaciones,
        })
<<<<<<< HEAD
        return redirect('verificar_equipo')
    return render(request, 'entrega/reporte.html', {
        'clientes': clientes_registrados,
        'equipos': equipos_registrados
    })
=======
        mensaje = 'Registro exitoso'
        return redirect('comprobante_entrega')
    return render(request, 'entrega/reporte.html', {'mensaje': mensaje})

def comprobante_entrega(request):
    # Muestra el último registro como comprobante
    comprobante = equipos_entregados[-1] if equipos_entregados else None
    return render(request, 'entrega/comprobante.html', {'comprobante': comprobante})
>>>>>>> e99703f12acfebac4082134a4372a8fcc356d997
