from django.shortcuts import render, get_object_or_404, redirect
from .models import Factura, Detalle_Factura
from .forms import FacturaForm, DetalleFacturaForm
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required
def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'lista_facturas.html', {'facturas': facturas})

@login_required
def crear_factura(request):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        if factura_form.is_valid():
            factura = factura_form.save()
            return redirect('detalle_factura', id=factura.ID_Factura)
    else:
        factura_form = FacturaForm()
    
    return render(request, 'crear_factura.html', {'factura_form': factura_form})

def actualizar_factura(request, id):
    factura = get_object_or_404(Factura, ID_Factura=id)
    
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST, instance=factura)
        if factura_form.is_valid():
            factura_form.save()
            return redirect('detalle_factura', id=factura.ID_Factura)
    else:
        factura_form = FacturaForm(instance=factura)
    
    return render(request, 'actualizar_factura.html', {'factura_form': factura_form, 'factura': factura})

@login_required
def eliminar_factura(request, id):
    factura = get_object_or_404(Factura, ID_Factura=id)
    factura.delete()
    return redirect('lista_facturas')

@login_required
def detalle_factura(request, id):
    factura = get_object_or_404(Factura, ID_Factura=id)
    detalles = Detalle_Factura.objects.filter(Factura=factura)

    if request.method == 'POST':
        detalle_form = DetalleFacturaForm(request.POST)
        if detalle_form.is_valid():
            detalle = detalle_form.save(commit=False)
            detalle.Factura = factura
            detalle.save()
            return redirect('detalle_factura', id=factura.ID_Factura)
    else:
        detalle_form = DetalleFacturaForm()

    return render(request, 'detalle_factura.html', {
        'factura': factura,
        'detalles': detalles,
        'detalle_form': detalle_form
    })
