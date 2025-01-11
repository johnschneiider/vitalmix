from django.urls import path
from . import views
app_name = "compras"
urlpatterns = [
    path('', views.registrar_compra, name='registrar_compra'),
    path('vers/', views.ver_compras, name='ver_compras'),
    path('editar/<int:compra_id>/', views.editar_compra, name='editar_compra'),
    path('eliminar/<int:compra_id>/', views.eliminar_compra, name='eliminar_compra'),
]
