# Finanzas Claras

## Descripción
Finanzas Claras es una plataforma web de consultoría financiera desarrollada con Python y Django. Está orientada a Pymes y personas que están comenzando a organizar sus finanzas personales. La página ofrece servicios, artículos de blog, tutoriales, plantillas gratuitas y un sistema de mensajería.

## Tecnologías utilizadas
- Python 3.13
- Django 6.0.2
- Bootstrap 5
- SQLite
- Pillow
- django-ckeditor

## Requisitos previos
- Python 3.x instalado
- pip instalado

## Instalación y ejecución

1. Clonar el repositorio:
git clone https://github.com/waltercoder84735/TuPrimeraPagina-Licitra.git

2. Entrar a la carpeta del proyecto:
cd TuPrimeraPagina-Licitra

3. Instalar las dependencias:
pip install -r requirements.txt

4. Ejecutar las migraciones:
python manage.py migrate

5. Crear un superusuario para acceder al panel de administración:
python manage.py createsuperuser

6. Iniciar el servidor:
python manage.py runserver

7. Abrir el navegador en:
http://127.0.0.1:8000/

## Estructura del proyecto
- **core**: app principal con servicios, blog, tutoriales, plantillas y buscador
- **accounts**: app de usuarios con registro, login, perfil y cambio de contraseña
- **mensajes**: app de mensajería para que los usuarios contacten al administrador

## Orden para probar las funcionalidades

1. Ir a /about para ver la página "Acerca de mí"
2. Ir a /blog para ver los artículos publicados y hacer clic en "Leer más"
3. Ir a /servicios para ver los servicios disponibles
4. Ir a /tutoriales para ver los tutoriales disponibles
5. Ir a /plantillas para ver y descargar las plantillas gratuitas
6. Ir a /accounts/registro para crear un usuario nuevo
7. Ir a /accounts/login para iniciar sesión
8. Ir a /mensajes/enviar para enviar un mensaje al administrador
9. Ir a /mensajes/buzon para ver los mensajes recibidos (requiere login)
10. Ir a /accounts/perfil para ver y editar el perfil de usuario
11. Ir a /admin para acceder al panel de administración (requiere superusuario)

## Funcionalidades principales
- Registro, login y logout de usuarios
- Perfil de usuario con avatar, biografía y fecha de nacimiento
- Cambio de contraseña desde el perfil
- CRUD completo de artículos del blog (crear, leer, editar, eliminar)
- Buscador general en la página de inicio
- Sistema de mensajería para contactar al administrador
- Panel de administración con todos los modelos registrados
- Herencia de templates con Bootstrap 5

## Autor
Walter Licitra