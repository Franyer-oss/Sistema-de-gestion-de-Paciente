from django.db import models
from paciente.models import Paciente
from medico.models import Medico

class Historia_Clinica(models.Model):
    ID_Historia = models.AutoField(primary_key=True)
    Paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    Medico = models.OneToOneField(Medico, on_delete=models.CASCADE, null=True, blank=True)
    Fecha_Apertura = models.DateField()
    Observaciones_Generales = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Historia_Clinica'

    def __str__(self):
        return f"Historia Clínica de {self.Paciente}"


class Diagnostico(models.Model):
    ID_Diagnostico = models.AutoField(primary_key=True)
    Historia_Clinica = models.ForeignKey(Historia_Clinica, on_delete=models.CASCADE)
    Fecha = models.DateField(auto_now_add=True)
    Descripcion = models.TextField()

    class Meta:
        db_table = 'Diagnostico'

    def __str__(self):
        return f"Diagnóstico {self.ID_Diagnostico}"


class Tratamiento(models.Model):
    ID_Tratamiento = models.AutoField(primary_key=True)
    Diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)
    Descripcion = models.TextField()
    Duracion = models.CharField(max_length=100)

    class Meta:
        db_table = 'Tratamiento'

    def __str__(self):
        return f"Tratamiento {self.ID_Tratamiento}"


class Examen_Laboratorio(models.Model):
    Historia_Clinica = models.ForeignKey(Historia_Clinica, on_delete=models.CASCADE)
    ID_Examen = models.AutoField(primary_key=True)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    Tipo_Examen = models.CharField(max_length=100)
    Fecha = models.DateField(auto_now_add=True)
    Archivo = models.ImageField(upload_to="Imganes_reultados/", null = True, blank =True)
    Resultado = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Examen_Laboratorio'

    def __str__(self):
        return f"Examen {self.Tipo_Examen} - {self.Paciente}"

