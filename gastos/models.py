# gastos/models.py
from django.db import models

class Gasto(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
