from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Medico, Area_Medica
from django.contrib.auth.decorators import login_required

@login_required
def ListaMedicos(request):
    # Obtiene todos los médicos como diccionarios
    medicos = Medico.objects.select_related("Area").all()
    return render(request, "Medico.html", {
        "medicos": medicos
    })
@login_required
def listaArea(request):
    # Obtiene todos los médicos como diccionarios
    areas = list(Medico.objects.values())
    return JsonResponse(Area_Medica, safe=False)

@login_required
def CreateMedico(request):
    areas = Area_Medica.objects.all()  # Para mostrar las áreas médicas disponibles

    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        especialidad = request.POST['especialidad']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        area_id = request.POST['area']
        NombreArea =  request.POST['NombreArea']
        Descripcion =  request.POST['Descripcion']
        
        # Crear médico
        medico = Medico.objects.create(
            Nombre=nombre,
            Apellido=apellido,
            Especialidad=especialidad,
            Telefono=telefono,
            Correo=correo,
            Area_id=area_id
        )

        
        areamedica= Area_Medica.objects.create(
            Nombre_Area = NombreArea,
            Descripcion = Descripcion
        )
        return redirect('ListaMedicos')  # Redirige al listado de médicos
    return render(request, 'CrearMedico.html', {'areas': areas})

@login_required
def EditMedico(request, id):
    medico = get_object_or_404(Medico, ID_Medico=id)
    areas = Area_Medica.objects.all()  # Para mostrar las áreas médicas disponibles
    
    if request.method == 'POST':
        # Actualizar datos del médico
        medico.Nombre = request.POST['nombre']
        medico.Apellido = request.POST['apellido']
        medico.Especialidad = request.POST['especialidad']
        medico.Telefono = request.POST['telefono']
        medico.Correo = request.POST['correo']
        
        # Actualizar área médica
        area_id = request.POST['area']  # El ID del área seleccionada
        medico.Area_id = area_id
        
        medico.save()
        return redirect('ListaMedicos')  # Redirige al listado de médicos
    
    return render(request, 'EditarMedico.html', {
        'medico': medico,
        'areas': areas
    })
@login_required
def DeleteMedico(request, id):
    pacientes=get_object_or_404(Medico, ID_Medico = id)
    pacientes.delete()
    return redirect('ListaMedicos')
