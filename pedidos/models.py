from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    PAGO_OPCIONES = [
        ('anticipado', 'Pago Anticipado'),
        ('contraentrega', 'Contra Entrega'),
    ]
    
    VENDEDORES = [
        ('John', 'John Jimenez'),
        ('Johanna', 'Johanna García'),
        ('Tatiana', 'Tatiana Rengifo'),
        ('Tienda Virtual', 'Tienda Virtual'),
    ]
    
    PRODUCTOS = [
        ('Frutos Rojos', 'Frutos Rojos'),
        ('Batido Verde', 'Batido Verde'),
        
    ]
    
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    cantidad_paquetes = models.PositiveIntegerField()
    fecha_entrega = models.DateField()
    producto = models.CharField(choices=PRODUCTOS, default="Batido Verde", max_length=20)
    fecha_ingreso = models.DateField(auto_now_add=True)
    nombre_vendedor = models.CharField(max_length=100, choices=VENDEDORES, default="Tienda Virtual")
    metodo_pago = models.CharField(max_length=20, choices=PAGO_OPCIONES, default="Contra Entrega")
    pagado = models.BooleanField(default=False)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos_vendedor')

    def __str__(self):
        return f"Pedido de {self.nombre_cliente} - {self.cantidad_paquetes} paquetes"