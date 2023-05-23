from django.urls import path
from totem_cliente.views import *

urlpatterns = [
    #home
    path('', home, name="home"),
    
    #restaurante
    path('buscar_restaurantes', buscar_restaurantes, name="buscar_restaurantes"),
        
    #produto
    path('listar_produtos/<int:restaurante_id>', listar_produtos, name="listar_produtos"),
    path('buscar_produtos', buscar_produtos, name="buscar_produtos"),
    path('adicionar_produto/<int:produto_id>', adicionar_produto, name="adicionar_produto"),
    path('remover_produto/<int:produto_id>', remover_produto, name="remover_produto"),
    
    #carrinho
    path('carrinho', listar_carrinho, name="listar_carrinho"),
    
    #pagamento
    path('pagamento', listar_pagamento, name="listar_pagamento")
]