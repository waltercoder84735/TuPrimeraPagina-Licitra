from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Mensaje
from .forms import MensajeForm

class EnviarMensajeView(LoginRequiredMixin, View):
    def get(self, request):
        form = MensajeForm()
        return render(request, 'mensajes/enviar_mensaje.html', {'form': form})
    
    def post(self, request):
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return render(request, 'mensajes/enviar_mensaje.html', {'form': MensajeForm(), 'exito': True})
        return render(request, 'mensajes/enviar_mensaje.html', {'form': form})

class BuzonView(LoginRequiredMixin, View):
    def get(self, request):
        mensajes = Mensaje.objects.all()
        return render(request, 'mensajes/buzon.html', {'mensajes': mensajes})