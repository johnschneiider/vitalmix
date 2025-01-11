import random
from django.shortcuts import render, redirect
from pedidos.models import Pedido
from .models import ResultadoRuleta

def girar_ruleta(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    
    # Opciones de la ruleta
    opciones = ['Descuento 10%', 'Descuento 20%', 'Envío Gratis', 'Sin Premio']
    resultado = random.choice(opciones)  # Elige aleatoriamente
    
    # Guarda el resultado asociado al pedido
    ResultadoRuleta.objects.create(pedido=pedido, resultado=resultado)
    
    # Redirige al agradecimiento o a otra página
    return redirect('pedidos:agradecimiento', nombre_cliente=pedido.nombre_cliente)



