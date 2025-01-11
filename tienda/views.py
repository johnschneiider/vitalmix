from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carrito, ListaDeseos
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from .models import Producto
from .forms import ProductoForm, ImagenProductoForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito, Producto, Pedido
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pedido, PedidoDetalle, Carrito, Producto
from django.db import transaction

def tienda(request):
    producto = Producto.objects.first()  # Suponiendo que tienes un único producto de momento
    return render(request, 'tienda/tienda.html', {'producto': producto})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user, producto=producto)
    carrito.cantidad += 1
    carrito.save()
    return redirect('tienda:carrito')

def ver_carrito(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    # Calcular el total por cada item
    for item in carrito_items:
        item.total_producto = item.cantidad * item.producto.precio
    # Calcular el total del carrito
    total_carrito = sum(item.total_producto for item in carrito_items)

    return render(request, 'tienda/carrito.html', {
        'carrito_items': carrito_items,
        'total_carrito': total_carrito,  # Total del carrito
    })


def agregar_a_deseos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    ListaDeseos.objects.get_or_create(usuario=request.user, producto=producto)
    return redirect('tienda:lista_deseos')

def lista_deseos(request):
    deseos = ListaDeseos.objects.filter(usuario=request.user)
    return render(request, 'tienda/lista_deseos.html', {'deseos': deseos})

def agregar_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        imagen_form = ImagenProductoForm(request.POST, request.FILES)
        if producto_form.is_valid():
            producto = producto_form.save()
            if imagen_form.is_valid():
                imagen = imagen_form.save(commit=False)
                imagen.producto = producto
                imagen.save()
            return redirect('tienda:tienda')  # Redirige a la vista principal de la tienda
    else:
        producto_form = ProductoForm()
        imagen_form = ImagenProductoForm()

    return render(request, 'tienda/agregar_producto.html', {'producto_form': producto_form, 'imagen_form': imagen_form})




def actualizar_carrito(request):
    if request.method == 'POST':
        for item in Carrito.objects.filter(usuario=request.user):
            cantidad_key = f'cantidad_{item.id}'  # Para obtener la cantidad enviada
            if cantidad_key in request.POST:
                nueva_cantidad = int(request.POST[cantidad_key])
                # Verificamos si la cantidad es válida y no supera el stock
                if nueva_cantidad <= item.producto.stock:
                    item.cantidad = nueva_cantidad
                    item.save()
    return redirect('tienda:carrito')



def eliminar_del_carrito(request, item_id):
    # Obtener el objeto carrito por su ID y usuario
    item = get_object_or_404(Carrito, id=item_id, usuario=request.user)
    item.delete()  # Eliminar el carrito
    return redirect('tienda:carrito') 


def finalizar_compra(request):
    if request.method == 'POST':
        # Lógica para finalizar la compra y crear el pedido
        carrito_items = Carrito.objects.filter(usuario=request.user)
        if carrito_items.exists():
            pedido = Pedido.objects.create(usuario=request.user, total=sum([item.total_producto for item in carrito_items]))
            
            # Crear el pedido con los artículos del carrito
            for item in carrito_items:
                pedido.detalles.create(producto=item.producto, cantidad=item.cantidad, precio=item.producto.precio)
            
            # Vaciar el carrito después de crear el pedido
            carrito_items.delete()
            
            return redirect('tienda:confirmar_compra')  # Redirigir a una página de confirmación de compra
    
    return render(request, 'tienda/finalizar_compra.html')


@login_required
def procesar_compra(request):
    # Verificamos que el usuario tenga productos en el carrito
    carrito_items = Carrito.objects.filter(usuario=request.user)
    if not carrito_items.exists():
        messages.error(request, "Tu carrito está vacío.")
        return redirect('tienda:carrito')

    # Calculamos el total del carrito
    total_carrito = sum(item.producto.precio * item.cantidad for item in carrito_items)
    
    # Obtener el teléfono desde el formulario
    telefono = request.POST.get('telefono')

    # Creamos el pedido y los detalles dentro de una transacción para asegurar consistencia de datos
    with transaction.atomic():
        # Crear el pedido
        pedido = Pedido.objects.create(
            usuario=request.user,
            total=total_carrito,
            estado='pendiente',
            telefono=telefono  # Guardamos el teléfono en el pedido
        )

        # Crear los detalles del pedido para cada producto en el carrito
        for item in carrito_items:
            PedidoDetalle.objects.create(
                pedido=pedido,
                producto=item.producto,
                cantidad=item.cantidad,
                precio=item.producto.precio,
                total=item.cantidad * item.producto.precio
            )

            # Actualizar el stock del producto
            item.producto.stock -= item.cantidad
            item.producto.save()

        # Vaciar el carrito después de realizar la compra
        carrito_items.delete()

    # Mensaje de éxito y redirección
    messages.success(request, "¡Compra realizada con éxito!")
    return redirect('tienda:confirmacion_pedido')

def confirmacion_pedido(request):
    return render(request, 'tienda/confirmacion_pedido.html')