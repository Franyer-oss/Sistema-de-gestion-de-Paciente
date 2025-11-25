from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaCitas, name='ListaCitas'),
    path('eventos/', views.calendario, name='calendario'),  # Para obtener los eventos
]