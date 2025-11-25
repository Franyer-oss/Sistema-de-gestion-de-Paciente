from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required

@login_required
def ListaPaciente(request):
    pacientes = list(Paciente.objects.values())
    return render(request, 'Paciente.html',{
        'pacientes': pacientes
    })
@login_required
def CreatePaciente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        Tipo_Documento= request.POST['Tipo_Documento']
        N_documento = request.POST['N_documento']
        F_Nacimiento = request.POST['F_Nacimiento']
        genero = request.POST['genero']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        estadocivil = request.POST['estadocivil']
        Paciente.objects.create(
            Nombre=nombre, Apellido=apellido, Tipo_Documento=Tipo_Documento, Numero_Documento=N_documento, Fecha_Nacimiento=F_Nacimiento, Genero=genero, Direccion=direccion, Telefono=telefono, Correo=correo, Estado_Civil=estadocivil
        )
        return redirect(ListaPaciente)
    return render(request, 'CrearPacientes.html')
@login_required
def EditPaciente(request, id):
    pacientes=get_object_or_404(Paciente, ID_Paciente = id)
    tipo_documentos=Paciente.TIPO_DOCUMENTO
    estado_civil=Paciente.ESTADOCIVIL
    genero=Paciente.GENERO
    if request.method == 'POST':
        pacientes.Nombre = request.POST['nombre']
        pacientes.Apellido = request.POST['apellido']
        pacientes.Tipo_Documento= request.POST['T_Documento']
        pacientes.Numero_Documento = request.POST['N_documento']
        pacientes.Fecha_Nacimiento = request.POST['F_Nacimiento']
        pacientes.Genero = request.POST['genero']
        pacientes.Direccion = request.POST['direccion']
        pacientes.Telefono = request.POST['telefono']
        pacientes.Correo = request.POST['correo']
        pacientes.Estado_Civil = request.POST['estadocivil']
        pacientes.save()
        return redirect(ListaPaciente)
    return render(request, 'EditarPacientes.html',{
        'pacientes': pacientes,
        'tipo_documentos': tipo_documentos,
        'estado_civil': estado_civil,
        'genero':genero
    })
@login_required
def DeletePaciente(request, id):
    pacientes=get_object_or_404(Paciente, ID_Paciente = id)
    pacientes.delete()
    return redirect(ListaPaciente)

@login_required
def exportar_paciente_pdf(request, id_paciente):
    paciente = Paciente.objects.get(ID_Paciente=id_paciente)

    # Configurar la respuesta HTTP como PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Paciente_{paciente.Nombre}_{paciente.Apellido}.pdf"'

    # Crear el lienzo PDF
    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, 750, "Información del Paciente")
    p.line(180, 745, 430, 745)
    p.setFont("Helvetica", 12)

    # Posiciones iniciales
    y = 720

    datos = [
        ("Nombre:", f"{paciente.Nombre} {paciente.Apellido}"),
        ("Tipo de Documento:", paciente.get_Tipo_Documento_display()),
        ("Número de Documento:", paciente.Numero_Documento),
        ("Fecha de Nacimiento:", paciente.Fecha_Nacimiento.strftime("%d/%m/%Y")),
        ("Género:", paciente.get_Genero_display()),
        ("Dirección:", paciente.Direccion),
        ("Teléfono:", paciente.Telefono),
        ("Correo:", paciente.Correo or "No registrado"),
        ("Estado Civil:", paciente.get_Estado_Civil_display()),
        ("Fecha de Registro:", paciente.Fecha_Registro.strftime("%d/%m/%Y %H:%M")),
    ]

    for campo, valor in datos:
        p.drawString(100, y, f"{campo} {valor}")
        y -= 25

    p.showPage()
    p.save()
    return response
