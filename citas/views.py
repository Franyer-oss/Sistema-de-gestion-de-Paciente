from django.shortcuts import render
from django.http import JsonResponse
from .models import Cita
from django.contrib.auth.decorators import login_required

@login_required
def ListaCitas(request):
    return render(request, 'calendario.html')

@login_required
def calendario(request):
    # Aquí obtenemos todas las citas
    citas = Cita.objects.all()

    # Convertimos las citas a un formato que FullCalendar pueda entender (en este caso, un JSON)
    eventos = []
    for cita in citas:
        evento = {
            'title': f"{cita.Paciente} con {cita.Medico}",
            'start': f"{cita.Fecha}T{cita.Hora}",
            'end': f"{cita.Fecha}T{cita.Hora}",  # Si quieres que tenga una duración específica, modifica esto
            'description': cita.Motivo,
            'estado': cita.Estado,
        }
        eventos.append(evento)

    # Respondemos con los datos de las citas en formato JSON
    return JsonResponse(eventos, safe=False)

