from django.urls import path
from . import views

app_name = 'ruleta'

urlpatterns = [
    path('girar/<int:pedido_id>/', views.girar_ruleta, name='girar_ruleta'),
]
