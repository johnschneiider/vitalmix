from django.urls import path
from . import views

app_name = 'calculadora'

urlpatterns = [
    path('', views.calcular_ingredientes, name='calcular_ingredientes'),
]
