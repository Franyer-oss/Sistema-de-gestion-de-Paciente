from django.shortcuts import render, redirect, get_object_or_404
from .models import Historia_Clinica, Diagnostico, Examen_Laboratorio
from .forms import DiagnosticoForm, Examen_Laboratorio_Form
from paciente.models import Paciente
from medico.models import Medico
from django.contrib.auth.decorators import login_required

@login_required
def ListaHistorial(request):
    pacientes = Paciente.objects.all()
    paciente_id = request.GET.get('paciente')
    listahistorial = Historia_Clinica.objects.select_related('Paciente')
    diagnosticos = Diagnostico.objects.select_related('Historia_Clinica')
    examenes = Examen_Laboratorio.objects.all()

    if paciente_id and paciente_id.isdigit():
        listahistorial = listahistorial.filter(Paciente_id=int(paciente_id))
        examenes = examenes.filter(Paciente_id=int(paciente_id))
        diagnosticos = diagnosticos.filter(Historia_Clinica__Paciente_id=paciente_id)

    return render(request, 'Historial.html', {
        'listahistorial': listahistorial,
        'examenes': examenes,
        'pacientes': pacientes,
        'diagnosticos':diagnosticos,
        'paciente_id': paciente_id or ''
    })
@login_required
def EliminarDiagnostico(request, id):
    # Obtener el diagnóstico a eliminar
    diagnostico = get_object_or_404(Diagnostico, ID_Diagnostico=id)
    
    # Eliminar el diagnóstico
    diagnostico.delete()
    
    # Redirigir de vuelta a la página de edición del historial
    return redirect('EditarHistorial', id=diagnostico.Historia_Clinica.ID_Historia)



@login_required
def CrearHistorial(request):
    if request.method == 'POST':
        id_paciente = request.POST['paciente']
        paciente = get_object_or_404(Paciente, pk=id_paciente)
        fecha_apertura = request.POST['fecha_apertura']
        observaciones_generales = request.POST.get('observaciones_generales', '')
        Historia_Clinica.objects.create(
            Paciente=paciente,
            Fecha_Apertura=fecha_apertura,
            Observaciones_Generales=observaciones_generales
        )
        return redirect('ListaHistorial')

    pacientes = Paciente.objects.all()
    return render(request, 'CrearHistorial.html', {'pacientes': pacientes})

@login_required
def EditarHistorial(request, id):
    historial = get_object_or_404(Historia_Clinica, ID_Historia=id)

    # Siempre carga lista de datos
    diagnosticos = Diagnostico.objects.filter(Historia_Clinica=historial)
    examenes = Examen_Laboratorio.objects.filter(Historia_Clinica=historial)
    medicos = Medico.objects.all()


    if request.method == 'POST':

        formulario = request.POST.get('formulario')   


        if formulario == "historial":
            historial.Medico_id = request.POST.get("medico")
            historial.Fecha_Apertura = request.POST.get("fecha_apertura")
            historial.Observaciones_Generales = request.POST.get("observaciones")
            historial.save()
            return redirect('ListaHistorial')

        elif formulario == "diagnostico":
            form = DiagnosticoForm(request.POST)
            if form.is_valid():
                nuevo_diag = form.save(commit=False)
                nuevo_diag.Historia_Clinica = historial
                nuevo_diag.save()
            return redirect('ListaHistorial')

    else:
        form = DiagnosticoForm()  # Formulario vacío para diagnóstico

    return render(request, 'EditarHistorial.html', {
        'historial': historial,
        'diagnosticos': diagnosticos,
        'medicos': medicos,
        'examenes': examenes,
        'form': form
    })


@login_required
def EliminarHistorial(request, id):
    historial = get_object_or_404(Historia_Clinica, ID_Historia=id)
    historial.delete()
    return redirect('ListaHistorial')

def VerExamenes(request, id):
    Examenes = Examen_Laboratorio.objects.filter(Paciente_id=id)
    return render(request, 'VerExamenes.html', {
        'Examenes': Examenes,
    })

def AdjuntarExamen(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    historial = get_object_or_404(Historia_Clinica, Paciente=paciente)

    if request.method == 'POST':
        form = Examen_Laboratorio_Form(request.POST, request.FILES)
        if form.is_valid():
            examen = form.save(commit=False)
            examen.Paciente = paciente          # Asignar paciente actual
            examen.Historia_Clinica = historial # Asignar la historia clínica
            examen.save()
            return redirect('ListaHistorial')
    else:
        form = Examen_Laboratorio_Form()

    return render(request, 'AdjuntarExamen.html', {
        'form': form,
        'historial': historial,
        'paciente': paciente
    })
@login_required
def EliminarExamen(request, id):
    historial = get_object_or_404(Examen_Laboratorio, ID_Examen=id)
    historial.delete()
    return redirect('ListaHistorial')
