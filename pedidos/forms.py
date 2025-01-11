# pedidos/forms.py
from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'telefono', 'cantidad_paquetes',
                  'fecha_entrega', 'nombre_vendedor', 'metodo_pago']
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
        }
