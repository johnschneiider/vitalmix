# autenticacion/models.py

from django.contrib.auth.models import User
from django.db import models
import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    barrio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fecha_cumpleaños = models.DateField(null=True, blank=True)
    pregunta1 = models.CharField(max_length=255, blank=True, null=True)
    pregunta2 = models.CharField(max_length=255, blank=True, null=True)
    respuesta1 = models.CharField(max_length=255, blank=True, null=True)
    respuesta2 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.telefono}"