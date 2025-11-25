from django.db import models
from paciente.models import Paciente
from medico.models import Medico

class Usuario_Sistema(models.Model):
    ID_Usuario = models.AutoField(primary_key=True)
    Nombre_Usuario = models.CharField(max_length=50, unique=True)
    Contraseña = models.CharField(max_length=255)
    Rol = models.CharField(max_length=50)
    Paciente = models.OneToOneField(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    Medico = models.OneToOneField(Medico, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'Usuario_Sistema'

    def __str__(self):
        return self.Nombre_Usuario
