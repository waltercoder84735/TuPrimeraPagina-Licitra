from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.EnviarMensajeView.as_view(), name='enviar_mensaje'),
    path('buzon/', views.BuzonView.as_view(), name='buzon'),
]