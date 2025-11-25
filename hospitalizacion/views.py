from django.shortcuts import render, get_object_or_404, redirect
from .models import Hospitalizacion, Habitacion
from paciente.models import Paciente
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def lista_hospitalizaciones(request):
    hospitalizaciones = Hospitalizacion.objects.all()
    return render(request, 'lista_hospitalizaciones.html', {'hospitalizaciones': hospitalizaciones})

@login_required
def crear_hospitalizacion(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        habitacion_id = request.POST.get('habitacion')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        motivo = request.POST.get('motivo')
        
        paciente = Paciente.objects.get(id=paciente_id)
        habitacion = Habitacion.objects.get(id=habitacion_id)
        
        hospitalizacion = Hospitalizacion(
            Paciente=paciente,
            Habitacion=habitacion,
            Fecha_Ingreso=fecha_ingreso,
            Motivo=motivo
        )
        hospitalizacion.save()
        messages.success(request, 'Hospitalización creada con éxito.')
        return redirect('lista_hospitalizaciones')
    else:
        pacientes = Paciente.objects.all()
        habitaciones = Habitacion.objects.filter(Estado='Disponible')  # Solo habitaciones disponibles
        return render(request, 'crear_hospitalizacion.html', {'pacientes': pacientes, 'habitaciones': habitaciones})

@login_required
def actualizar_hospitalizacion(request, id):
    hospitalizacion = get_object_or_404(Hospitalizacion, id=id)
    
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        habitacion_id = request.POST.get('habitacion')
        fecha_salida = request.POST.get('fecha_salida')
        motivo = request.POST.get('motivo')
        
        paciente = Paciente.objects.get(id=paciente_id)
        habitacion = Habitacion.objects.get(id=habitacion_id)
        
        hospitalizacion.Paciente = paciente
        hospitalizacion.Habitacion = habitacion
        hospitalizacion.Fecha_Salida = fecha_salida
        hospitalizacion.Motivo = motivo
        hospitalizacion.save()
        messages.success(request, 'Hospitalización actualizada con éxito.')
        return redirect('lista_hospitalizaciones')
    else:
        pacientes = Paciente.objects.all()
        habitaciones = Habitacion.objects.filter(Estado='Disponible')  # Solo habitaciones disponibles
        return render(request, 'actualizar_hospitalizacion.html', {'hospitalizacion': hospitalizacion, 'pacientes': pacientes, 'habitaciones': habitaciones})

@login_required
def eliminar_hospitalizacion(request, id):
    hospitalizacion = get_object_or_404(Hospitalizacion, id=id)
    hospitalizacion.delete()
    messages.success(request, 'Hospitalización eliminada con éxito.')
    return redirect('lista_hospitalizaciones')
