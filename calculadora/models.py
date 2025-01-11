from django.db import models

class Paquete(models.Model):
    cantidad = models.PositiveIntegerField()

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    gramos_por_bolsita = models.FloatField()
