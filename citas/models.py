from django.db import models
from paciente.models import Paciente
from medico.models import Medico

class Cita(models.Model):
    ESTADOS = [
        ('Programada', 'Programada'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
        ('Pendiente', 'Pendiente'),
        ('En espera', 'En espera'),
    ]
    ID_Cita = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    Hora = models.TimeField()
    Motivo = models.TextField()
    Estado = models.CharField(max_length=50, choices=ESTADOS)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Cita'

    def __str__(self):
        return f"Cita {self.ID_Cita} - {self.Paciente} con {self.Medico}"
