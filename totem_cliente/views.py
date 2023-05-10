from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def listar_restaurantes(request):
    restaurantes = Restaurante.objects.order_by("nome").filter(ativo=True)

    return render(request, "totem_cliente/inicio.html", {"restaurantes": restaurantes})

def listar_produtos(request):
    produtos = Produto.objects.order_by("nome").filter(restaurante=request.GET.id, ativo=True)
    
    return render(request, "totem_cliente/produtos.html", {"produtos": produtos})