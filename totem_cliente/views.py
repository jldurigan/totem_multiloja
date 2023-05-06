from django.shortcuts import render
from django.http import HttpResponse

def listar_restaurantes(request):
    return render(request, "inicio.html")