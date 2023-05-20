from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from .models import *

def home(request):
    request.session.flush()
    restaurantes = Restaurante.objects.order_by("nome").filter(ativo=True)

    return render(request, "totem_cliente/home.html", {"restaurantes": restaurantes})

#produto
def listar_produtos(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, pk=restaurante_id)
    if 'restaurante' in request.session:
        request.session.clear()
    else:
        request.session['restaurante'] = [restaurante_id]
        
    produtos = Produto.objects.order_by("nome").filter(ativo=True, restaurante_id=restaurante_id)
    categorias = Categoria.objects.order_by("nome").filter(ativo=True, restaurante_id=restaurante_id)
    
    return render(request, "totem_cliente/produtos.html", {"restaurante": restaurante, "produtos": produtos, "categorias": categorias})

def adicionar_produto(request, produto_id):
    if 'restaurante' not in request.session:
        return JsonResponse({"Mensagem": "Ação inválida!"})
    
    # produto = get_object_or_404(Produto, pk=produto_id, restaurante=request.session['restaurante'][0])
        
    
    if 'carrinho' in request.session:
        request.session['carrinho'].insert(0, produto_id)
    else:
        request.session['carrinho'] = [produto_id]
        
    request.session.modified=True
    
    carrinho = []
    for item in request.session['carrinho']:
        carrinho.append[item]
    
    return JsonResponse(carrinho, safe=False)

def remover_produto(request, produto_id):
    if 'carrinho' in request.session:
        if produto_id in request.session['carrinho']:
            request.session['carrinho'].remove(produto_id)
        
    request.session.modified=True
    
    carrinho = list(Produto.objects.filter(pk__in=request.session['carrinho']))
    
    return JsonResponse(carrinho)

def listar_carrinho(request):
    # if 'carrinho' in request.session:
        
    return render(request, "totem_cliente/carrinho.html")

def listar_pagamento(request):
    return render(request, "totem_cliente/pagamento.html")