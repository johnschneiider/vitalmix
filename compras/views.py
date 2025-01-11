# compras/views.py
from django.shortcuts import render, redirect, redirect, get_object_or_404
from .models import Compra
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def registrar_compra(request):
    ingredientes = ['Pepino', 'Apio', 'Perejil', 'Piña', 'Manzana Verde']
    if request.method == 'POST':
        for ingrediente in ingredientes:
            cantidad = request.POST.get(f'cantidad_{ingrediente}')
            precio = request.POST.get(f'precio_{ingrediente}')
            if cantidad and precio:
                Compra.objects.create(
                    nombre_ingrediente=ingrediente,
                    cantidad_libras=cantidad,
                    precio=precio,
                    fecha_compra=timezone.now()
                )
        # Después de registrar, muestra el formulario nuevamente
        return render(request, 'compras/compras.html', {
            'ingredientes': ingredientes,
            'mensaje_exito': "Compra registrada con éxito.",
        })
    # Renderiza el formulario
    return render(request, 'compras/compras.html', {
        'ingredientes': ingredientes,
    })


# compras/views.py
def ver_compras(request):
    compras = Compra.objects.all().order_by('-fecha_compra')
    return render(request, 'compras/ver_compras.html', {'compras': compras})


def editar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    if request.method == 'POST':
        compra.cantidad_libras = request.POST.get('cantidad_libras')
        compra.precio = request.POST.get('precio')
        compra.save()
        return redirect('compras:ver_compras')
    return render(request, 'compras/editar_compra.html', {'compra': compra})

def eliminar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    if request.method == 'POST':
        compra.delete()
        return redirect('compras:ver_compras')
    return render(request, 'compras/eliminar_compra.html', {'compra': compra})