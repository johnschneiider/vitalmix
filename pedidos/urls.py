from django.urls import path
from . import views
app_name = 'pedidos'  # Esto define el namespace
urlpatterns = [
    path('', views.registrar_pedido, name='registrar_pedido'),
    path('listar/', views.listar_pedidos, name='listar_pedidos'),
    path('marcar_pagado/<int:pedido_id>/', views.marcar_pagado, name='marcar_pagado'),
    path('eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('mis_ventas/', views.mis_ventas, name='mis_ventas'),
   path('agradecimiento/<str:nombre_cliente>/', views.agradecimiento, name='agradecimiento'),


]
