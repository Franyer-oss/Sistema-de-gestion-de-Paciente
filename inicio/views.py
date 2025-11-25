from django.shortcuts import render
from paciente.models import Paciente
from citas.models import Cita
from hospitalizacion.models import Hospitalizacion
from django.contrib.auth.decorators import login_required

@login_required
def Principal(request):
    total_pacientes = Paciente.objects.all().count
    total_hospitalizacion = Hospitalizacion.objects.all().count
    citas = Cita.objects.select_related('Paciente', 'Medico').all
    citas_pendientes= Cita.objects.filter(Estado = 'Pendiente').count()
    return render(request, "Principal.html",
                  {
                    'total_pacientes': total_pacientes,
                    'total_hospitalizacion': total_hospitalizacion,
                    'citas_pendientes':citas_pendientes,
                    'informacion': citas
                  })
# Create your views here.