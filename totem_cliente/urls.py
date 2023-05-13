from django.urls import path
from totem_cliente.views import *

urlpatterns = [
    path('', listar_restaurantes, name="listar_restaurantes"),
    
    #produto
    path('listar_produtos/<int:restaurante_id>', listar_produtos, name="listar_produtos"),
    path('visualizar_produto/<int:produto_id>', visualizar_produto, name="visualizar_produto"),
    
    #carrinho
    path('carrinho', listar_carrinho, name="listar_carrinho"),
    path('add_carrinho/<int:produto_id>', add_carrinho, name="add_carrinho"),
    
    #pagamento
    path('pagamento', listar_pagamento, name="listar_pagamento")
]