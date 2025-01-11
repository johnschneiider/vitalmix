from django.contrib import admin
from .models import Producto, Pedido, PedidoDetalle

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'telefono', 'cantidad','fecha_creacion', 'total', 'estado')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('usuario__username','telefono')
    
    

@admin.register(PedidoDetalle)
class PedidoDetalleAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'precio', 'total')
    search_fields = ('pedido__id', 'producto__nombre')
