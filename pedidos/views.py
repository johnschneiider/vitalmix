from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Pedido
from django.db.models import Sum

@login_required
def registrar_pedido(request):
    return render(request, 'pedidos/registrar_pedido.html')


from django.shortcuts import render, redirect
from .forms import PedidoForm
from .models import Pedido
import random

@login_required
def registrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            # Crea una instancia del pedido, pero no lo guarda aún
            pedido = form.save(commit=False)
            # Asigna el vendedor al pedido
            pedido.vendedor = request.user
            # Ahora guarda el pedido
            pedido.save()
            return redirect('ruleta:girar_ruleta', pedido_id=pedido.id)
    else:
        form = PedidoForm()
    
    return render(request, 'pedidos/registrar_pedido.html', {'form': form})

@login_required
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/listar_pedidos.html', {'pedidos': pedidos})

# pedidos/views.py
from django.shortcuts import get_object_or_404

@login_required
def marcar_pagado(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.pagado = True
    pedido.save()
    return redirect('pedidos:listar_pedidos')

@login_required
def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.delete()  # Elimina el pedido
    return redirect('pedidos:listar_pedidos')


@login_required
def mis_ventas(request):
    pedidos = Pedido.objects.filter(vendedor=request.user)
    clientes_sin_pagar = pedidos.filter(pagado=False)
    total_ventas = pedidos.aggregate(total=Sum('cantidad_paquetes'))
    
    context = {
        'pedidos': pedidos,
        'clientes_sin_pagar': clientes_sin_pagar,
        'total_ventas': total_ventas,
    }
    return render(request, 'pedidos/mis_ventas.html', context)

@login_required
def agradecimiento(request, nombre_cliente):
    return render(request, 'pedidos/agradecimiento.html', {'nombre_cliente': nombre_cliente})