from django.db import models
from ckeditor.fields import RichTextField

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20)  # "Pyme" o "Personal"
    precio_referencia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='articulos/', null=True, blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    tipo_interes = models.CharField(max_length=20)  # "Pyme" o "Personal"
    mensaje = models.TextField()
    fecha_contacto = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Tutorial(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    url_video = models.URLField()
    tipo = models.CharField(max_length=20)  # "Pyme" o "Personal"
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Plantilla(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    url_descarga = models.URLField()
    tipo = models.CharField(max_length=20)  # "Pyme" o "Personal"

    def __str__(self):
        return self.nombre
