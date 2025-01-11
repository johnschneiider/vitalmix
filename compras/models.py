# compras/models.py
from django.db import models

class Compra(models.Model):
    nombre_ingrediente = models.CharField(max_length=100)
    cantidad_libras = models.DecimalField(max_digits=6, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_compra = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_ingrediente} - {self.cantidad_libras} libras - ${self.precio}"
