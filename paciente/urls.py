from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListaPaciente, name='ListaPaciente'),
    path('crear/', views.CreatePaciente, name='CreatePaciente'),
    path('editar/<int:id>/', views.EditPaciente, name='EditPaciente'), 
    path('eliminar/<int:id>/', views.DeletePaciente, name='DeletePaciente'),
    path('paciente/pdf/<int:id_paciente>/', views.exportar_paciente_pdf, name='exportar_paciente_pdf'),
]
