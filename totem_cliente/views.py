from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *

def listar_restaurantes(request):
    restaurantes = Restaurante.objects.order_by("nome").filter(ativo=True)

    return render(request, "totem_cliente/inicio.html", {"restaurantes": restaurantes})

#produto
def listar_produtos(request, restaurante_id):
    categorias = Categoria.objects.order_by("nome").filter(ativo=True, visivel=True, restaurante_id=restaurante_id)
    
    produtos = Produto.objects.order_by("nome").filter(restaurante_id=restaurante_id, visivel=True, ativo=True)
    
    return render(request, "totem_cliente/produtos.html", {"produtos": produtos, "categorias": categorias})

def adicionar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    
    adicionais = ProdutoParteProduto.objects.filter(produto_pai=produto, ativo=True)
    
    return render(request, "totem_cliente/adicionar_produto.html", {"produto": produto, "adicionais": adicionais})

#carrinho
def add_carrinho(request):
    carrinho = 'carrinho'
    item = {
        'produto': '',
        'quantidade': '',
        'preco': '',
        'observacoes': ''
    }
    
    if carrinho in request.session[carrinho]:
        request.session[carrinho].insert(0, item)
    else:
        request.session[carrinho]=[item]
    
    # produto = get_object_or_404(Produto, pk=produto_id)
    # carrinho = Carrinho(restaurante=produto.restaurante, valor_total=0)
    # carrinho.save()
    # item_carrinho = ItemCarrinho(carrinho=carrinho, produto=produto, quantidade=1)
    # item_carrinho.save()
    
    # # itens_carrinho = ItemCarrinho.objects.filter(carr)
    return render(request, "totem_cliente/carrinho.html", {"item_carrinho": item_carrinho})

def listar_carrinho(request):
    return render(request, "totem_cliente/carrinho.html")

def listar_pagamento(request):
    return render(request, "totem_cliente/pagamento.html")