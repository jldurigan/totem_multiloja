from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_restaurantes, name="listar_restaurantes"),
    path('produtos/<int:restaurante_id>', views.listar_produtos, name="produtos"),
    path('carrinho', views.listar_carrinho, name="listar_carrinho"),
    path('pagamento', views.listar_pagamento, name="listar_pagamento")
]