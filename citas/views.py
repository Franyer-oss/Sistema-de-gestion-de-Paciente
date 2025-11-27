from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Cita
import json

@login_required
def ListaCitas(request):
    return render(request, 'calendario.html')

@login_required
def calendario(request):
    citas = Cita.objects.all()
    eventos = []
    for cita in citas:
        eventos.append({
            'id': cita.ID_Cita,
            'title': f"{cita.Paciente} con {cita.Medico}",
            'start': f"{cita.Fecha}T{cita.Hora}",
            'end': f"{cita.Fecha}T{cita.Hora}",
            'description': cita.Motivo,
            'estado': cita.Estado,
        })
    return JsonResponse(eventos, safe=False)

