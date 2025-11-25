from django.db import models

class Area_Medica(models.Model):
    ID_Area = models.AutoField(primary_key=True)
    Nombre_Area = models.CharField(max_length=100)
    Descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Area_Medica'

    def __str__(self):
        return self.Nombre_Area


class Medico(models.Model):
    ID_Medico = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Especialidad = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=20)
    Correo = models.CharField(max_length=100)
    Area = models.ForeignKey(Area_Medica, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Medico'

    def __str__(self):
        return f"Dr. {self.Nombre} {self.Apellido} del area de {self.Area.Nombre_Area}"

