# reportes/views.py
from django.shortcuts import render
from pedidos.models import Pedido
from compras.models import Compra
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
import random
from django.contrib.auth.decorators import login_required

@login_required

def mostrar_reportes(request):
    # Clientes más frecuentes
    clientes_frecuentes = (
        Pedido.objects
        .values('nombre_cliente', 'telefono')
        .annotate(total_pedidos=Sum('id'))
        .order_by('-total_pedidos')[:10]
    )
    
    nombres_clientes = [cliente['nombre_cliente'] for cliente in clientes_frecuentes]
    total_pedidos_clientes = [cliente['total_pedidos'] for cliente in clientes_frecuentes]

    # Ventas por vendedor y por mes
    ventas_por_vendedor_mes = (
        Pedido.objects
        .annotate(mes=TruncMonth('fecha_ingreso'))
        .values('nombre_vendedor', 'mes')
        .annotate(total_ventas=Count('id'), total_paquetes=Sum('cantidad_paquetes'))
        .order_by('mes', 'nombre_vendedor')
    )
    
    vendedores = list(set([venta['nombre_vendedor'] for venta in ventas_por_vendedor_mes]))
    total_ventas_vendedores = {vendedor: [] for vendedor in vendedores}
    meses_ventas = []

    for venta in ventas_por_vendedor_mes:
        mes_str = venta['mes'].strftime("%B")
        if mes_str not in meses_ventas:
            meses_ventas.append(mes_str)
        total_ventas_vendedores[venta['nombre_vendedor']].append(venta['total_paquetes'])
    
    # Clientes que no han pagado
    clientes_no_pagados_por_mes = (
        Pedido.objects
        .filter(pagado=False)
        .annotate(mes=TruncMonth('fecha_ingreso'))
        .values('mes')
        .annotate(total_no_pagados=Count('id'))
        .order_by('mes')
    )
    
    meses_no_pagados = [cliente['mes'].strftime("%B") for cliente in clientes_no_pagados_por_mes]
    total_no_pagados = [cliente['total_no_pagados'] for cliente in clientes_no_pagados_por_mes]

    # Suma de costos de ingredientes y cantidad de libras compradas por mes
    costos_por_mes = (
        Compra.objects
        .annotate(mes=TruncMonth('fecha_compra'))
        .values('mes')
        .annotate(total_costos=Sum('precio'), total_libras=Sum('cantidad_libras'))
        .order_by('mes')
    )

    meses_costos = [compra['mes'].strftime("%B") for compra in costos_por_mes]
    total_costos = [compra['total_costos'] for compra in costos_por_mes]
    total_libras_compradas = [compra['total_libras'] for compra in costos_por_mes]

    context = {
        'nombres_clientes': nombres_clientes,
        'total_pedidos_clientes': total_pedidos_clientes,
        'vendedores': vendedores,
        'total_ventas_vendedores': total_ventas_vendedores,
        'meses_ventas': meses_ventas,
        'meses_no_pagados': meses_no_pagados,
        'total_no_pagados': total_no_pagados,
        'meses_costos': meses_costos,
        'total_costos': total_costos,
        'total_libras_compradas': total_libras_compradas,
    }
    return render(request, 'reportes/mostrar_reportes.html', context)
