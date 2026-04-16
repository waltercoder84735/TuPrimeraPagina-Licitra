from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Perfil
from .forms import RegistroForm, PerfilForm

class RegistroView(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, 'accounts/registro.html', {'form': form})
    
    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(usuario=usuario)
            login(request, usuario)
            return redirect('inicio')
        return render(request, 'accounts/registro.html', {'form': form})

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')
        return render(request, 'accounts/login.html', {'error': 'Usuario o contraseña incorrectos'})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('inicio')

class PerfilView(LoginRequiredMixin, View):
    def get(self, request):
        perfil, created = Perfil.objects.get_or_create(usuario=request.user)
        return render(request, 'accounts/perfil.html', {'perfil': perfil})

class EditarPerfilView(LoginRequiredMixin, View):
    def get(self, request):
        perfil, created = Perfil.objects.get_or_create(usuario=request.user)
        form = PerfilForm(instance=perfil)
        return render(request, 'accounts/editar_perfil.html', {'form': form})
    
    def post(self, request):
        perfil, created = Perfil.objects.get_or_create(usuario=request.user)
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
        return render(request, 'accounts/editar_perfil.html', {'form': form})