from django import forms
from .models import Factura, Detalle_Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['Paciente', 'Fecha_Emision', 'Total']

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = Detalle_Factura
        fields = ['Descripcion', 'Cantidad', 'Precio_Unitario', 'Subtotal']
