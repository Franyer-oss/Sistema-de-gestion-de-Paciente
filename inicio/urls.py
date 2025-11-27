from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.Principal, name="Principal"), 
    path('crear_cita/', views.crear_cita, name='crear_cita'),
    path('actualizar_cita/<int:cita_id>/', views.actualizar_cita, name='actualizar_cita'),
    path('eliminar_cita/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
    path('hospitalizacion/', include('hospitalizacion.urls')),
    path('facturacion/', include('facturacion.urls')),
    path('historiales/', include('historial.urls')),
    path('pacientes/', include('paciente.urls')), 
    path('medicos/', include('medico.urls')),
    path('citas/' , include ('citas.urls')),
]