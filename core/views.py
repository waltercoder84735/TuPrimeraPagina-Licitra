from django.shortcuts import render
from .models import Servicio, Articulo, Cliente, Tutorial, Plantilla
from .forms import ServicioForm, ArticuloForm, ClienteForm, TutorialForm, PlantillaForm, BusquedaClienteForm, BusquedaGeneralForm

def inicio(request):
    form = BusquedaGeneralForm(request.GET or None)
    resultados = []
    categoria = None
    if form.is_valid():
        categoria = form.cleaned_data['categoria']
        busqueda = form.cleaned_data['busqueda']
        if categoria == 'servicios':
            resultados = Servicio.objects.filter(nombre__icontains=busqueda)
        elif categoria == 'tutoriales':
            resultados = Tutorial.objects.filter(nombre__icontains=busqueda)
        elif categoria == 'plantillas':
            resultados = Plantilla.objects.filter(nombre__icontains=busqueda)
    return render(request, 'inicio.html', {'form': form, 'resultados': resultados, 'categoria': categoria})

def servicios(request):
    lista = Servicio.objects.all()
    form = ServicioForm()
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'servicios.html', {'servicios': lista, 'form': form})

def blog(request):
    articulos = Articulo.objects.all()
    form = ArticuloForm()
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'blog.html', {'articulos': articulos, 'form': form})

def tutoriales(request):
    lista = Tutorial.objects.all()
    form = TutorialForm()
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tutoriales.html', {'tutoriales': lista, 'form': form})

def plantillas(request):
    lista = Plantilla.objects.all()
    form = PlantillaForm()
    if request.method == 'POST':
        form = PlantillaForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'plantillas.html', {'plantillas': lista, 'form': form})

def contacto(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contacto.html', {'form': ClienteForm(), 'exito': True})
    return render(request, 'contacto.html', {'form': form})

def buscar_cliente(request):
    resultados = []
    form = BusquedaClienteForm(request.GET or None)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        resultados = Cliente.objects.filter(nombre__icontains=nombre)
    return render(request, 'buscar_cliente.html', {'form': form, 'resultados': resultados})
