from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *

def listar_restaurantes(request):
    restaurantes = Restaurante.objects.order_by("nome").filter(ativo=True)

    return render(request, "totem_cliente/inicio.html", {"restaurantes": restaurantes})

#produto
def listar_produtos(request, restaurante_id):
    produtos = Produto.objects.order_by("nome").filter(ativo=True, restaurante_id=restaurante_id)
    
    return render(request, "totem_cliente/listar_produtos.html", {"produtos": produtos})

def visualizar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    
    return render(request, "totem_cliente/visualizar_produto.html", {"produto": produto})

#carrinho
def add_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    carrinho = Carrinho(restaurante=produto.restaurante, valor_total=0)
    carrinho.save()
    item_carrinho = ItemCarrinho(carrinho=carrinho, produto=produto, quantidade=1)
    item_carrinho.save()
    
    itens_carrinho = ItemCarrinho.objects.filter(carr)
    return render(request, "totem_cliente/carrinho.html", {"item_carrinho": item_carrinho})

def listar_carrinho(request):
    return render(request, "totem_cliente/carrinho.html")

def listar_pagamento(request):
    return render(request, "totem_cliente/pagamento.html")