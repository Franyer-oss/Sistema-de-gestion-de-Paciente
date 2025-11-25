from django.db import models
from paciente.models import Paciente

class Habitacion(models.Model):
    ID_Habitacion = models.AutoField(primary_key=True)
    Numero = models.CharField(max_length=10)
    Tipo = models.CharField(max_length=50)
    Estado = models.CharField(max_length=20)

    class Meta:
        db_table = 'Habitacion'

    def __str__(self):
        return f"Habitación {self.Numero}"


class Hospitalizacion(models.Model):
    ID_Hospitalizacion = models.AutoField(primary_key=True)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    Fecha_Ingreso = models.DateField()
    Fecha_Salida = models.DateField(null=True, blank=True)
    Motivo = models.TextField()

    class Meta:
        db_table = 'Hospitalizacion'

    def __str__(self):
        return f"Hospitalización {self.ID_Hospitalizacion} - {self.Paciente}"
