from django.urls import path
from . import views  # Certifique-se de que há uma view configurada

urlpatterns = [
    path('', views.inventory, name='inventory'),  # Exemplo de uma rota
]
