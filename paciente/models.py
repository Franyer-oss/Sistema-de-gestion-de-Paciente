from django.db import models

class Paciente(models.Model):
    TIPO_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
    ]

    ESTADOCIVIL = [
        ('S', 'Soltero/a'),
        ('C', 'Casado/a'),
        ('V', 'Viudo/a'),
        ('D', 'Divorciado/a'),
    ]

    GENERO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    ID_Paciente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Tipo_Documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO)
    Numero_Documento = models.IntegerField(unique=True)
    Fecha_Nacimiento = models.DateField()
    Genero = models.CharField(max_length=1, choices=GENERO)
    Direccion = models.CharField(max_length=150)
    Telefono = models.CharField(max_length=20)
    Correo = models.CharField(max_length=100, null=True, blank=True)
    Estado_Civil = models.CharField(max_length=2, choices=ESTADOCIVIL)
    Fecha_Registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Paciente'
        ordering = ['Nombre']

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"
