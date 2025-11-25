from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_hospitalizaciones, name='lista_hospitalizaciones'),
    path('crear/', views.crear_hospitalizacion, name='crear_hospitalizacion'),
    path('editar/<int:id>/', views.actualizar_hospitalizacion, name='actualizar_hospitalizacion'),
    path('eliminar/<int:id>/', views.eliminar_hospitalizacion, name='eliminar_hospitalizacion'),
]
