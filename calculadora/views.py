# calculadora/views.py
from django.shortcuts import render
from pedidos.models import Pedido  # Asegúrate de importar el modelo Pedido
from django.contrib.auth.decorators import login_required

@login_required
def calcular_ingredientes(request):
    resultado = {}
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Verifica que las fechas estén presentes
        if fecha_inicio and fecha_fin:
            # Obtén los pedidos dentro del rango de fechas
            pedidos_en_rango = Pedido.objects.filter(fecha_entrega__range=[fecha_inicio, fecha_fin])
            total_paquetes = sum(pedido.cantidad_paquetes for pedido in pedidos_en_rango)

            # Definir los gramos de cada ingrediente por bolsita
            ingredientes = {
                'Pepino': 60,  # gramos por bolsita
                'Apio': 30,
                'Perejil': 10,
                'Piña': 70,
                'Manzana Verde': 30,
            }

            # Calcular la cantidad total de cada ingrediente en libras
            for ingrediente, gramos_por_bolsita in ingredientes.items():
                gramos_totales = gramos_por_bolsita * 5 * total_paquetes  # 5 bolsitas por paquete
                libras = gramos_totales / 453.592  # Convertir a libras
                resultado[ingrediente] = round(libras, 2)

            # Agrega la información del total de paquetes al resultado
            resultado['Total de paquetes'] = total_paquetes

        return render(request, 'calculadora/calculadora.html', {'resultado': resultado})

    return render(request, 'calculadora/calculadora.html')
