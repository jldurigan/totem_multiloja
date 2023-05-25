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
    path('alterar_quantidade', alterar_quantidade, name="alterar_quantidade"),
    
    #carrinho
    path('carrinho', listar_carrinho, name="listar_carrinho"),
    
    #pagamento
    path('pagamento', listar_pagamento, name="listar_pagamento"),
    
    ##pedido
    path('gerar_pedido', gerar_pedido, name="gerar_pedido")
]