from django.urls import path
from totem_cliente.views import *

urlpatterns = [
    path('', home, name="home"),
    
    #produto
    path('listar_produtos/<int:restaurante_id>', listar_produtos, name="listar_produtos"),
    path('adicionar_produto/<int:produto_id>', adicionar_produto, name="adicionar_produto"),
    
    #carrinho
    path('carrinho', listar_carrinho, name="listar_carrinho"),
    
    #pagamento
    path('pagamento', listar_pagamento, name="listar_pagamento")
]