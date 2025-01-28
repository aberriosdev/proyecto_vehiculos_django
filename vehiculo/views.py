from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.contrib.auth import login, logout
from django.contrib.contenttypes.models import ContentType
from .forms import VehiculoForm
from .models import Vehiculo


def index(request):
    return render(request, 'index.html')

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            content_type = ContentType.objects.get_for_model(Vehiculo)
            permiso = Permission.objects.get(content_type=content_type, codename='visualizar_catalogo')
            user.user_permissions.add(permiso)
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'vehiculo/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})