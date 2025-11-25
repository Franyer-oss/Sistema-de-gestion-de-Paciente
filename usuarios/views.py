from django.shortcuts import render, redirect
from .models import Usuario_Sistema
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegistroForm
from http.client import HTTPResponse

def Registrar_usuarios(request):
    if request.method == 'GET':
        return render(request, 'registrar.html', {
            'forms': RegistroForm()
        })
    else:
        form = RegistroForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("Login")

        return render(request, 'registrar.html', {
            'forms': form
        })
    
def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return render(request, 'login.html', {
                'error': 'Debes llenar ambos campos'
            })

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('Principal')
        else:
            return render(request, 'login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })



    

