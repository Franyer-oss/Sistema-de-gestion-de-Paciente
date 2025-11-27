from django.shortcuts import render, get_object_or_404, redirect
from paciente.models import Paciente
from hospitalizacion.models import Hospitalizacion
from django.contrib.auth.decorators import login_required
from citas.models import Cita
from paciente.models import Paciente
from medico.models import Medico



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
# CREAR CITA
@login_required
def crear_cita(request):
    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()

    if request.method == 'POST':
        paciente = request.POST['paciente']
        medico = request.POST['medico']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        motivo = request.POST['motivo']
        estado = request.POST['estado']

        if not fecha or not hora:
            error = "Debe ingresar una fecha y una hora válidas."
            return render(request, "crear_cita.html", {
                "pacientes": pacientes,
                "error": error
            })

        Cita.objects.create(
            Paciente_id=paciente,
            Medico_id=medico,
            Fecha=fecha,
            Hora=hora,
            Motivo=motivo,
            Estado=estado
        )
        return redirect('Principal')

    return render(request, 'crear_cita.html', {
        'pacientes': pacientes,
        'medicos': medicos
    })


# ACTUALIZAR CITA
@login_required
def actualizar_cita(request, cita_id):
    cita = get_object_or_404(Cita, ID_Cita=cita_id)
    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()

    if request.method == 'POST':
        cita.Paciente = request.POST['paciente']
        cita.Medico = request.POST['medico']
        cita.Fecha = request.POST['fecha']
        cita.Hora = request.POST['hora']
        cita.Motivo = request.POST['motivo']
        cita.Estado = request.POST['estado']
        cita.save()

        return redirect('Principal')

    return render(request, 'actualizar_cita.html', {
        'cita': cita,
        'pacientes': pacientes,
        'medicos': medicos
    })


# ELIMINAR CITA
@login_required
def eliminar_cita(request, cita_id):
    cita = get_object_or_404(Cita, ID_Cita=cita_id)
    cita.delete()
    return redirect('Principal')