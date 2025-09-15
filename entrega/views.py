from django.shortcuts import render, redirect

# Simulación de datos en memoria
equipos_entregados = []

def verificar_equipo(request):
    estado = None
    cliente = ''
    if request.method == 'GET' and 'cliente' in request.GET:
        cliente = request.GET.get('cliente')
        equipo = next((e for e in equipos_entregados if e['cliente'] == cliente), None)
        if equipo:
            estado = equipo
        else:
            estado = 'No encontrado'
    return render(request, 'entrega/verificar.html', {'estado': estado, 'cliente': cliente})

def reporte_entrega(request):
    mensaje = ''
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
        mensaje = 'Registro exitoso'
        return redirect('comprobante_entrega')
    return render(request, 'entrega/reporte.html', {'mensaje': mensaje})

def comprobante_entrega(request):
    # Muestra el último registro como comprobante
    comprobante = equipos_entregados[-1] if equipos_entregados else None
    return render(request, 'entrega/comprobante.html', {'comprobante': comprobante})