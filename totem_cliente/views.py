from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from .models import *

def home(request):
    request.session.flush()
    restaurantes = Restaurante.objects.order_by("nome").filter(ativo=True)

    return render(request, "totem_cliente/home.html", {"restaurantes": restaurantes})

def buscar_restaurantes(request):
    resultado = {
        "Retorno": [],
        "Mensagem": "",
        "Sucesso": False
    }
    
    if request.method != "POST":
        resultado["Mensagem"] = ["Ação inválida!"]
    else:
        restaurantes = Restaurante.objects.order_by("nome").filter(ativo=True)
        
        if "nome" in request.POST:
            nome = request.POST["nome"]
            if nome:
                restaurantes = restaurantes.filter(nome__icontains=nome)
                for restaurante in restaurantes:
                    resultado["Retorno"].insert(0, restaurante.id)
                resultado["Sucesso"] = True
                
    return JsonResponse(resultado, safe=False)
            
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

def buscar_produtos(request):
    resultado = {
        "Retorno": [],
        "Mensagem": "",
        "Sucesso": False
    }
    
    if request.method != "POST" or "restaurante" not in request.session:
        resultado["Mensagem"] = ["Ação inválida!"]
    else:
        produtos = Produto.objects.order_by("nome").filter(ativo=True, restaurante=request.session["restaurante"][0])
        
        if "nome" in request.POST:
            nome = request.POST["nome"]
            if nome:
                produtos = produtos.filter(nome__icontains=nome)
                for produto in produtos:
                    resultado["Retorno"].insert(0, produto.id)
                resultado["Sucesso"] = True
                
    return JsonResponse(resultado, safe=False)

def adicionar_produto(request, produto_id):
    resultado = {
        "Retorno": [],
        "Mensagem": "",
        "Sucesso": False
    }
    
    if 'restaurante' not in request.session:
        resultado["Mensagem"] = ["Ação inválida!"]
    else:
        # produto = get_object_or_404(Produto, pk=produto_id, restaurante=request.session['restaurante'][0])
            
        if 'carrinho' in request.session:
            request.session['carrinho'].insert(0, produto_id)
        else:
            request.session['carrinho'] = [produto_id]
            
        request.session.modified=True
        
        for item in request.session['carrinho']:
            resultado["Retorno"].insert(0, item)
        
        resultado["Sucesso"] = True
    
    return JsonResponse(resultado, safe=False)

def remover_produto(request, produto_id):
    if 'carrinho' in request.session:
        if produto_id in request.session['carrinho']:
            request.session['carrinho'].remove(produto_id)
        
    request.session.modified=True
    
    carrinho = list(Produto.objects.filter(pk__in=request.session['carrinho']))
    
    return JsonResponse(carrinho)

def listar_carrinho(request):
    resultado = {
        "Retorno": [],
        "Mensagem": "",
        "Sucesso": False
    }
    
    if 'carrinho' not in request.session:
        return JsonResponse("")
        
    return render(request, "totem_cliente/carrinho.html")

def listar_pagamento(request):
    return render(request, "totem_cliente/pagamento.html")