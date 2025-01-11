from django.urls import path
from . import views
app_name="reportes"
urlpatterns = [
    path('', views.mostrar_reportes, name='mostrar_reportes'),
]
