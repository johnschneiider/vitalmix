from django.db import models
from pedidos.models import Pedido

class ResultadoRuleta(models.Model):
    opciones = [
        ('Descuento 10%', 'Descuento 10%'),
        ('Descuento 20%', 'Descuento 20%'),
        ('Envío Gratis', 'Envío Gratis'),
        ('Sin Premio', 'Sin Premio'),
    ]
    
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='resultado_ruleta')
    resultado = models.CharField(max_length=50, choices=opciones)
    fecha_giro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Resultado: {self.resultado} para Pedido {self.pedido.id}"
