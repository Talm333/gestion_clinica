from django.shortcuts import render, redirect
from .models import Entrega
from recepcion.models import Equipo
from diagnostico.models import Diagnostico
from .forms import EntregaForm

def verificar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    
    cliente = ''
    
    if request.method == 'GET' and 'cliente' in request.GET:
        cliente = request.GET.get('cliente')
        if cliente:
            # buscamos por nombre de cliente
            equipos = Equipo.objects.filter(cliente__icontains=cliente)
        else:
            equipos = Equipo.objects.all()
    else:
        equipos = Equipo.objects.all()

    return render(request, 'entrega/verificar.html', {'equipos': equipos, 'cliente': cliente})

def reporte_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    
    mensaje = ''
    
    initial_data = {}
    if request.GET.get('diagnostico'):
        initial_data['diagnostico'] = request.GET.get('diagnostico')
    
    form = EntregaForm(initial=initial_data)
    
    if request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            form.instance.estado = 'ENTREGADO'
            entrega = form.save()
            mensaje = 'Registro exitoso'
            return redirect('comprobante_entrega', id=entrega.id)
            
    return render(request, 'entrega/reporte.html', {'mensaje': mensaje, 'form': form})

def comprobante_entrega(request, id):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    
    # busqueda manual
    try:
        comprobante = Entrega.objects.select_related('diagnostico').get(id=id)
    except Entrega.DoesNotExist:
        return redirect('listado_entregas')
    
    return render(request, 'entrega/comprobante.html', {'comprobante': comprobante})

def listado_entregas(request):
    if not request.session.get('autenticado'):
        return redirect('/login/login.html')
    
    entregas = Entrega.objects.all()
    return render(request, 'entrega/listado.html', {'entregas': entregas})
