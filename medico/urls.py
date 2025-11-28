from . import views
from django.urls import path


urlpatterns = [
    path('', views.ListaMedicos, name='ListaMedicos'),
    path('crear/', views.CreateMedico, name='CreateMedico'),
    path('editar/<int:id>/', views.EditMedico, name='EditMedico'), 
    path('eliminar/<int:id>/', views.DeleteMedico, name='DeleteMedico'),
    path('areas/', views.listaArea, name='listaArea'),
]