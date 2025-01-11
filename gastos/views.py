# gastos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Gasto
from django.contrib.auth.decorators import login_required

@login_required

# Vista para registrar un nuevo gasto
def registrar_gasto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        costo = request.POST.get('costo')
        if nombre and costo:
            Gasto.objects.create(nombre=nombre, costo=costo)
            return redirect('gastos:ver_gastos')
    return render(request, 'gastos/registrar_gasto.html')

# Vista para ver y listar gastos
def ver_gastos(request):
    gastos = Gasto.objects.all().order_by('-fecha')
    return render(request, 'gastos/ver_gastos.html', {'gastos': gastos})

# Vista para editar un gasto existente
def editar_gasto(request, gasto_id):
    gasto = get_object_or_404(Gasto, id=gasto_id)
    if request.method == 'POST':
        gasto.nombre = request.POST.get('nombre')
        gasto.costo = request.POST.get('costo')
        gasto.save()
        return redirect('gastos:ver_gastos')
    return render(request, 'gastos/editar_gasto.html', {'gasto': gasto})

# Vista para eliminar un gasto
def eliminar_gasto(request, gasto_id):
    gasto = get_object_or_404(Gasto, id=gasto_id)
    if request.method == 'POST':
        gasto.delete()
        return redirect('gastos:ver_gastos')
    return render(request, 'gastos/eliminar_gasto.html', {'gasto': gasto})
