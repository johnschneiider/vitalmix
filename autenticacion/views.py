from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
from .models import UserProfile, User
from django.db import IntegrityError


def prueba_mensajes(request):
    messages.error(request, 'Prueba: este es un mensaje de error.')
    return render(request, 'autenticacion/inicio_sesion.html')



def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirige a la página principal de Vialmix
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'autenticacion/inicio_sesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')  # Redirige a la página de inicio de sesión



def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        password_confirm = request.POST.get('password_confirm', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        barrio = request.POST.get('barrio', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        fecha_cumpleaños = request.POST.get('fecha_cumpleaños', '').strip()

        # Validación de contraseñas
        if password != password_confirm:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'autenticacion/registro.html')

        # Validar si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso. Por favor, elige otro.')
            return render(request, 'autenticacion/registro.html')

        # Validar campos obligatorios
        if not telefono or not barrio or not direccion or not fecha_cumpleaños:
            messages.error(request, 'Por favor, completa todos los campos obligatorios.')
            return render(request, 'autenticacion/registro.html')

        # Crear usuario y perfil
        try:
            user = User.objects.create_user(username=username, password=password)
            UserProfile.objects.create(
                user=user,
                telefono=telefono,
                barrio=barrio,
                direccion=direccion,
                fecha_cumpleaños=fecha_cumpleaños
            )
            messages.success(request, 'Usuario registrado exitosamente. Puedes iniciar sesión.')
            return redirect('autenticacion:inicio_sesion')


        except IntegrityError:
            messages.error(request, 'Hubo un error con el registro. Por favor, intenta de nuevo.')
        except Exception as e:
            messages.error(request, f'Ocurrió un error inesperado: {e}')

    return render(request, 'autenticacion/registro.html')










#--------------------------------------------------------------------------------

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile  # Suponiendo que tienes un modelo `Usuario` que almacena el teléfono y las preguntas de seguridad.
import random

def recuperar_contrasena(request):
    if request.method == 'POST':
        telefono = request.POST.get('telefono')
        try:
            # Busca al usuario por el teléfono
            usuario = UserProfile.objects.get(telefono=telefono)
            # Guarda el teléfono en la sesión para usarlo más adelante
            request.session['telefono'] = telefono
            return redirect('autenticacion:recuperar_preguntas')
        except UserProfile.DoesNotExist:
            messages.error(request, 'El número de teléfono no está registrado.')
    return render(request, 'autenticacion/recuperar_contrasena.html')

def recuperar_preguntas(request):
    telefono = request.session.get('telefono')
    if not telefono:
        return redirect('autenticacion:recuperar_contrasena')

    try:
        usuario = UserProfile.objects.get(telefono=telefono)
    except UserProfile.DoesNotExist:
        messages.error(request, 'Ha ocurrido un error. Intenta de nuevo.')
        return redirect('autenticacion:recuperar_contrasena')

    if request.method == 'POST':
        respuesta1 = request.POST.get('respuesta1')
        respuesta2 = request.POST.get('respuesta2')

        # Validar respuestas
        if (respuesta1 == usuario.fecha_cumpleaños.strftime('%d/%m/%Y') and
            respuesta2 == usuario.barrio):
            # Respuestas correctas, redirige al usuario para cambiar la contraseña
            return redirect('autenticacion:cambiar_contrasena')
        else:
            messages.error(request, 'Las respuestas no coinciden.')

    # Generar opciones aleatorias para la fecha de cumpleaños
    fechas_random = [usuario.fecha_cumpleaños.strftime('%d/%m/%Y')]  # Correcta
    # Puedes agregar fechas aleatorias (esto es solo un ejemplo, puedes ajustar según tus necesidades)
    fechas_random += [
        '01/01/1990', '15/05/1985', '10/12/2000'
    ]
    random.shuffle(fechas_random)  # Barajar las opciones

    # Generar opciones aleatorias para el barrio
    barrios_random = [usuario.barrio]  # Correcto
    # Puedes agregar barrios aleatorios
    barrios_random += ['El Rodeo', 'Cristobal Colon', 'El Obrero']
    random.shuffle(barrios_random)  # Barajar las opciones

    return render(request, 'autenticacion/recuperar_preguntas.html', {
        'fechas_random': fechas_random,
        'barrios_random': barrios_random
    })




from django.contrib.auth.hashers import make_password

def cambiar_contrasena(request):
    telefono = request.session.get('telefono')
    if not telefono:
        messages.error(request, 'No se encontró una sesión válida. Por favor, inténtalo de nuevo.')
        return redirect('autenticacion:recuperar_contrasena')

    try:
        usuario = UserProfile.objects.get(telefono=telefono)
    except UserProfile.DoesNotExist:
        messages.error(request, 'Ha ocurrido un error. Intenta de nuevo.')
        return redirect('autenticacion:recuperar_contrasena')

    if request.method == 'POST':
        nueva_password = request.POST.get('nueva_password', '').strip()
        confirmar_password = request.POST.get('confirmar_password', '').strip()

        # Verifica que las contraseñas no estén vacías
        if not nueva_password or not confirmar_password:
            messages.error(request, 'Ambos campos de contraseña son obligatorios.')
            return render(request, 'autenticacion/cambiar_contrasena.html')

        # Validar si las contraseñas coinciden
        if nueva_password != confirmar_password:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif len(nueva_password) < 8:
            messages.error(request, 'La nueva contraseña debe tener al menos 8 caracteres.')
        else:
            # Cambiar la contraseña del usuario
            usuario.user.password = make_password(nueva_password)
            usuario.user.save()
            messages.success(request, 'Tu contraseña se ha cambiado exitosamente.')
            return redirect('autenticacion:inicio_sesion')

    return render(request, 'autenticacion/cambiar_contrasena.html')


