from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.Principal, name="Principal"), 
    path('hospitalizacion/', include('hospitalizacion.urls')),
    path('facturacion/', include('facturacion.urls')),
    path('historiales/', include('historial.urls')),
    path('pacientes/', include('paciente.urls')), 
    path('medicos/', include('medico.urls')),
    path('citas/' , include ('citas.urls')),
]