from django.db import models
from paciente.models import Paciente

class Factura(models.Model):
    ID_Factura = models.AutoField(primary_key=True)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Fecha_Emision = models.DateField()
    Total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Factura'

    def __str__(self):
        return f"Factura {self.ID_Factura} - {self.Paciente}"


class Detalle_Factura(models.Model):
    ID_Detalle = models.AutoField(primary_key=True)
    Factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    Descripcion = models.CharField(max_length=200)
    Cantidad = models.IntegerField()
    Precio_Unitario = models.DecimalField(max_digits=10, decimal_places=2)
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Detalle_Factura'

    def __str__(self):
        return f"Detalle {self.ID_Detalle} de Factura {self.Factura.ID_Factura}"
