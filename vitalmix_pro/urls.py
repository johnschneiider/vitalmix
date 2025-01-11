"""
URL configuration for vitalmix_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from autenticacion.urls import *

urlpatterns = [
    path('', include('home.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('calculadora/', include('calculadora.urls',  namespace='calculadora')),
    path('compras/', include('compras.urls')),
    path('gastos/', include('gastos.urls')),
    path('pedidos/', include('pedidos.urls', namespace='pedido')),
    path('reportes/', include('reportes.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('prueba/', prueba_mensajes, name='prueba_mensajes'),
     path('ruleta/', include('ruleta.urls')),
    path('tienda/', include('tienda.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)