from django.db import models
from paciente.models import Paciente
from medico.models import Medico

class Medicamento(models.Model):
    ID_Medicamento = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(null=True, blank=True)
    Presentacion = models.CharField(max_length=50)

    class Meta:
        db_table = 'Medicamento'

    def __str__(self):
        return self.Nombre


class Receta(models.Model):
    ID_Receta = models.AutoField(primary_key=True)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    Fecha = models.DateField()
    Observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Receta'

    def __str__(self):
        return f"Receta {self.ID_Receta} - {self.Paciente}"


class Detalle_Receta(models.Model):
    ID_Detalle = models.AutoField(primary_key=True)
    Receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    Medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    Dosis = models.CharField(max_length=100)
    Frecuencia = models.CharField(max_length=100)
    Duracion = models.CharField(max_length=100)

    class Meta:
        db_table = 'Detalle_Receta'

    def __str__(self):
        return f"{self.Medicamento.Nombre} - {self.Receta.ID_Receta}"

