from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def listar_restaurantes(request):
    restaurantes = Restaurante.objects.order_by("nome").filter(ativo=True)

    return render(request, "totem_cliente/inicio.html", {"restaurantes": restaurantes})

def listar_produtos(request):
    return render(request, "totem_cliente/produtos.html")

def listar_carrinho(request):
    return render(request, "totem_cliente/carrinho.html")

def listar_pagamento(request):
    return render(request, "totem_cliente/pagamento.html")
