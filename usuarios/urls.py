from . import views
from django.urls import path
urlpatterns=[
    path('', views.Registrar_usuarios, name="Registrar_usuarios"),
    path('login/', views.Login, name='Login'),
]