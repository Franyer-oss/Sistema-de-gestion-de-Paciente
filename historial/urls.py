from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListaHistorial, name="ListaHistorial"),
    path('crear/', views.CrearHistorial, name="CrearHistorial"),
    path('editar/<int:id>/', views.EditarHistorial, name="EditarHistorial"),
    path('eliminar/<int:id>/', views.EliminarHistorial, name="EliminarHistorial"),
    path('adjuntar_examen/<int:id>/', views.AdjuntarExamen, name='AdjuntarExamen'),
    path('VerExamenes/<int:id>/', views.VerExamenes, name="VerExamenes"),
    path('EliminarExamen/<int:id>/', views.EliminarExamen, name="EliminarExamen"),
    path('eliminar_diagnostico/<int:id>/', views.EliminarDiagnostico, name='EliminarDiagnostico'),
]