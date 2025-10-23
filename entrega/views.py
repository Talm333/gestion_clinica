from django.shortcuts import render, redirect
from .models import Entrega
from recepcion.models import equipo

def verificar_equipo(request):
    estado = None
    cliente = ''
    if request.method == 'GET' and 'cliente' in request.GET:
        cliente = request.GET.get('cliente')
        entrega = Entrega.objects.filter(cliente=cliente).first()
        if entrega:
            estado = entrega
        else:
            estado = 'No encontrado'
    return render(request, 'entrega/verificar.html', {'estado': estado, 'cliente': cliente})

def reporte_entrega(request):
    mensaje = ''
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        equipo_id = request.POST.get('equipo')
        diagnostico = request.POST.get('diagnostico')
        estado_final = request.POST.get('estado_final')
        observaciones = request.POST.get('observaciones')
        equipo_obj = equipo.objects.get(id=equipo_id)
        Entrega.objects.create(
            cliente=cliente,
            equipo=equipo_obj,
            diagnostico=diagnostico,
            estado_final=estado_final,
            observaciones=observaciones
        )
        mensaje = 'Registro exitoso'
        return redirect('comprobante_entrega')
    return render(request, 'entrega/reporte.html', {'mensaje': mensaje})

def comprobante_entrega(request):
    # Muestra el último registro como comprobante
    comprobante = Entrega.objects.last()
    return render(request, 'entrega/comprobante.html', {'comprobante': comprobante})
