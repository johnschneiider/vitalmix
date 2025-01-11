from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('deseos/', views.lista_deseos, name='lista_deseos'),
    path('deseos/agregar/<int:producto_id>/', views.agregar_a_deseos, name='agregar_a_deseos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('carrito/actualizar/', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra'),
    path('procesar/', views.procesar_compra, name='procesar_compra'),
    path('confirmacion/', views.confirmacion_pedido, name='confirmacion_pedido'),
]
