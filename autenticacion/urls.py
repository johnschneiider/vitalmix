from django.urls import path
from .views import inicio_sesion, cerrar_sesion, registrar_usuario
from django.contrib.auth import views as auth_views
from .views import *
from . import views

app_name = 'autenticacion'
urlpatterns = [
    path('inicio_sesion/', auth_views.LoginView.as_view(template_name='autenticacion/inicio_sesion.html'), name='inicio_sesion'),
    path('cerrar/', cerrar_sesion, name='cerrar_sesion'),
    path('registro/', registrar_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='inicio_sesion.html'), name='login'),
    path('prueba/', prueba_mensajes, name='prueba_mensajes'),
    path('recuperar_contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
    path('recuperar_preguntas/', views.recuperar_preguntas, name='recuperar_preguntas'),
    path('cambiar_contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),

    
    
]
