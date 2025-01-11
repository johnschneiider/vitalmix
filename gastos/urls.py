# gastos/urls.py
from django.urls import path
from . import views

app_name = 'gastos'

urlpatterns = [
    path('registrar/', views.registrar_gasto, name='registrar_gasto'),
    path('', views.ver_gastos, name='ver_gastos'),
    path('editar/<int:gasto_id>/', views.editar_gasto, name='editar_gasto'),
    path('eliminar/<int:gasto_id>/', views.eliminar_gasto, name='eliminar_gasto'),
]
