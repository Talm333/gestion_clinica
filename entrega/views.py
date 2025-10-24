from django.shortcuts import render, redirect
from .models import Entrega
from recepcion.models import Equipo
from diagnostico.models import Diagnostico

def verificar_equipo(request):
    estado = None
    cliente = ''
    if request.method == 'GET' and 'cliente' in request.GET:
        cliente = request.GET.get('cliente')
        entrega = Entrega.objects.filter(diagnostico__equipo__cliente=cliente).first()
        if entrega:
            estado = entrega
        else:
            estado = 'No encontrado'
    return render(request, 'entrega/verificar.html', {'estado': estado, 'cliente': cliente})

def reporte_entrega(request):
    mensaje = ''
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        diagnostico_id = request.POST.get('diagnostico')
        diagnostico_obj = Diagnostico.objects.get(id=diagnostico_id)
        Entrega.objects.create(
            diagnostico=diagnostico_obj
        )
        mensaje = 'Registro exitoso'
        return redirect('comprobante_entrega')
    return render(request, 'entrega/reporte.html', {'mensaje': mensaje})

def comprobante_entrega(request):
    # Muestra el último registro como comprobante
    comprobante = Entrega.objects.last()
    return render(request, 'entrega/comprobante.html', {'comprobante': comprobante})
