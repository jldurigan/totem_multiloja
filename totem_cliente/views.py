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
        resultado["Mensagem"] = "Ação inválida!"
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
        request.session['restaurante'] = restaurante_id
        
    produtos = Produto.objects.order_by("nome").filter(ativo=True, restaurante_id=restaurante_id)
    categorias = Categoria.objects.order_by("nome").filter(ativo=True, restaurante_id=restaurante_id)
    
    return render(request, "totem_cliente/produtos.html", {"restaurante": restaurante, "produtos": produtos, "categorias": categorias})

def buscar_produtos(request):
    resultado = {
        "Retorno": [],
        "Mensagem": "",
        "Sucesso": False
    }
    
    if request.method != "POST":
        resultado["Mensagem"] = "Ação inválida!"
    elif "restaurante" not in request.session:
        resultado["Mensagem"] = "Sessão encerrada, redirecionando para o início..."
    else:
        produtos = Produto.objects.order_by("nome").filter(ativo=True, restaurante=request.session["restaurante"])
        
        if "categoriaSelecionada" not in request.POST and "nome" not in request.POST:
            resultado["Mensagem"] = "Nenhum parâmetro de busca foi enviado"
        else:
            nome = request.POST["nome"]
            if "categoriaSelecionada" in request.POST:
                categoria = request.POST["categoriaSelecionada"]
            if nome:
                produtos = produtos.filter(nome__icontains=nome)
            if categoria:
                produtos = produtos.filter(categoria__in=categoria)
                
            if not produtos:
                resultado["Mensagem"] = "Nenhum produto encontrado"
            else:
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
        resultado["Mensagem"] = "Sessão encerrada, retornando ao início..."
    else:
        produto = Produto.objects.get(id=produto_id, restaurante=request.session['restaurante'])
        if not produto:
            resultado["Mensagem"] = "Produto inválido!"
        else:
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
    if 'restaurante' not in request.session:
        return JsonResponse({"Mensagem": "Sessão encerrada, retornando ao início..."})
    elif 'carrinho' not in request.session:
        return JsonResponse({"Mensagem": "Adicione um produto para continuar"})
    else:
        produtos = []
        for produto_id in request.session['carrinho']:
            produtos.insert(0, Produto.objects.get(id=produto_id))
        
        restaurante = Restaurante.objects.get(id=request.session["restaurante"])
        
        return render(request, "totem_cliente/carrinho.html", {"produtos": produtos, "restaurante": restaurante})

def listar_pagamento(request):
    return render(request, "totem_cliente/pagamento.html")