from django import forms
from .models import Servicio, Articulo, Cliente, Tutorial, Plantilla

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'tipo', 'precio_referencia']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'tipo']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'tipo_interes', 'mensaje']

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['nombre', 'descripcion', 'url_video', 'tipo']

class PlantillaForm(forms.ModelForm):
    class Meta:
        model = Plantilla
        fields = ['nombre', 'descripcion', 'url_descarga', 'tipo']

class BusquedaClienteForm(forms.Form):
    nombre = forms.CharField(label='Buscar cliente por nombre', max_length=100)
