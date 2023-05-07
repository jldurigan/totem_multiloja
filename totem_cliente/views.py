from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def listar_restaurantes(request):
    restaurantes = Restaurante.objects.all()

    return render(request, "totem_cliente/inicio.html", {"restaurantes": restaurantes})