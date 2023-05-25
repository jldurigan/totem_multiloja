import random
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from .models import *


def home(request):
    request.session.flush()
    restaurantes = Restaurante.objects.order_by("nome").filter(ativo=True)

    return render(request, "totem_cliente/home.html", {"restaurantes": restaurantes})


def buscar_restaurantes(request):
    resultado = {"Retorno": [], "Mensagem": "", "Sucesso": False}

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


# produto
def listar_produtos(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, pk=restaurante_id)

    if "restaurante" not in request.session:
        request.session["restaurante"] = restaurante_id

    ##listando os itens do carrinho caso o usuario volte da tela de editar quantidades
    carrinho = []
    if "produtos" in request.session:
        for item in request.session["produtos"]:
            carrinho.insert(0, item)

    produtos = Produto.objects.order_by("nome").filter(
        ativo=True, restaurante_id=restaurante_id
    )
    categorias = Categoria.objects.order_by("nome").filter(
        ativo=True, restaurante_id=restaurante_id
    )

    return render(
        request,
        "totem_cliente/produtos.html",
        {
            "restaurante": restaurante,
            "produtos": produtos,
            "categorias": categorias,
            "carrinho": carrinho.__len__,
        },
    )


def buscar_produtos(request):
    resultado = {"Retorno": [], "Mensagem": "", "Sucesso": False}

    if request.method != "POST":
        resultado["Mensagem"] = "Ação inválida!"
    elif "restaurante" not in request.session:
        resultado["Mensagem"] = "Sessão expirada, redirecionando para o início..."
    else:
        produtos = Produto.objects.order_by("nome").filter(
            ativo=True, restaurante=request.session["restaurante"]
        )

        if "categoriaSelecionada" not in request.POST and "nome" not in request.POST:
            resultado["Mensagem"] = "Nenhum parâmetro de busca foi enviado"
        else:
            if "categoriaSelecionada" in request.POST:
                categoria = request.POST["categoriaSelecionada"]
                if categoria:
                    produtos = produtos.filter(categoria=categoria)
            nome = request.POST["nome"]
            if nome:
                produtos = produtos.filter(nome__icontains=nome)

            if not produtos:
                resultado["Mensagem"] = "Nenhum produto encontrado"
            else:
                for produto in produtos:
                    resultado["Retorno"].insert(0, produto.id)

                resultado["Sucesso"] = True

    return JsonResponse(resultado, safe=False)


def adicionar_produto(request, produto_id):
    resultado = {"Retorno": [], "Mensagem": "", "Sucesso": False}

    if "restaurante" not in request.session:
        resultado["Mensagem"] = "Sessão expirada, retornando ao início..."
    else:
        produto = Produto.objects.get(
            id=produto_id, restaurante=request.session["restaurante"]
        )
        if not produto:
            resultado["Mensagem"] = "Produto inválido!"
        else:
            item = {str(produto_id): {"quantidade": 1, "preco": str(produto.preco)}}
            if "produtos" in request.session:
                if str(produto_id) in request.session["produtos"]:
                    resultado["Mensagem"] = "Produto já adicionado!"
                else:
                    request.session["produtos"].update(item)
            else:
                request.session["produtos"] = item

            request.session.modified = True

            for item_add in request.session["produtos"]:
                resultado["Retorno"].insert(0, item_add)

            resultado["Sucesso"] = True

    return JsonResponse(resultado, safe=False)


def remover_produto(request, produto_id):
    resultado = {"Retorno": [], "Mensagem": "", "Sucesso": False}
    if "restaurante" not in request.session:
        resultado["Mensagem"] = "Sessão expirada, retornando ao início..."
    else:
        produto = Produto.objects.get(
            id=produto_id, restaurante=request.session["restaurante"]
        )
        if not produto:
            resultado["Mensagem"] = "Produto inválido!"
        elif "produtos" not in request.session:
            resultado["Mensagem"] = "Não existem produtos adicionados!"
        elif str(produto_id) not in request.session["produtos"]:
            resultado["Mensagem"] = "O produto não foi adicionado!"
        else:
            request.session["produtos"].pop(str(produto_id))

            request.session.modified = True

            for item in request.session["produtos"]:
                resultado["Retorno"].insert(0, item)

            resultado["Sucesso"] = True

    return JsonResponse(resultado)


def alterar_quantidade(request):
    resultado = {"Retorno": [], "Mensagem": "", "Sucesso": False}
    if "restaurante" not in request.session:
        resultado["Mensagem"] = "Sessão expirada, retornando ao início..."
    else:
        produto = Produto.objects.get(
            id=request.POST.get("produto_id"),
            restaurante=request.session["restaurante"],
        )
        if not produto:
            resultado["Mensagem"] = "Produto inválido!"
        elif "produtos" not in request.session:
            resultado["Mensagem"] = "Não existem produtos adicionados!"
        elif request.POST.get("produto_id") not in request.session["produtos"]:
            resultado["Mensagem"] = "O produto não foi adicionado!"
        else:
            request.session["produtos"][request.POST.get("produto_id")].update(
                {"quantidade": request.POST.get("quantidade")}
            )
            request.session.modified = True
            resultado["Sucesso"] = True

    return JsonResponse(resultado)


def listar_carrinho(request):
    produtos = []
    if "produtos" in request.session:
        for produto_id in request.session["produtos"]:
            produto = Produto.objects.get(id=produto_id)
            produto.quantidade = (
                request.session["produtos"].get(produto_id).get("quantidade")
            )
            produtos.insert(0, produto)

    restaurante = Restaurante.objects.get(id=request.session["restaurante"])

    return render(
        request,
        "totem_cliente/carrinho.html",
        {"produtos": produtos, "restaurante": restaurante},
    )


def listar_pagamento(request):
    produtos = []
    total = 0.0
    if "produtos" in request.session:
        for produto_id in request.session["produtos"]:
            produto = Produto.objects.get(id=produto_id)
            produto.quantidade = (
                request.session["produtos"].get(produto_id).get("quantidade")
            )
            produtos.insert(0, produto)
            total += float(produto.preco) * int(produto.quantidade)

        request.session["total"] = total
        request.session.modified = True

    restaurante = Restaurante.objects.get(id=request.session["restaurante"])

    return render(
        request,
        "totem_cliente/pagamento.html",
        {"produtos": produtos, "restaurante": restaurante, "total": total},
    )


def realizar_pagamento(request):
    resultado = {"Retorno": [], "Mensagem": "", "Sucesso": False}

    if (
        "produtos" not in request.session
        or "restaurante" not in request.session
        or "total" not in request.session
    ):
        resultado["Mensagem"] = "Sessão expirada, retornando para o início..."
    else:
        sucesso_pagamento = True

        if not sucesso_pagamento:
            resultado["Mensagem"] = "Erro ao realizar o pagamento. Tente novamente"
        else:
            resultado["Sucesso"] = True

    return JsonResponse(resultado)


def gerar_pedido(request):
    resultado = {"Retorno": [], "Mensagem": "", "Sucesso": False}

    restaurante = Restaurante.objects.get(id=request.session["restaurante"])
    codigo_interno = str(random.randint(1, 999)).zfill(3)
    total = request.session["total"]
    observacoes = request.POST.get("observacoes")
    pedido = Pedido(
        codigo_interno=codigo_interno,
        restaurante=restaurante,
        total=total,
        observacoes=observacoes,
    )
    pedido.save()

    for produto_id in request.session["produtos"]:
        produto = Produto.objects.get(id=produto_id)
        produto.quantidade = (
            request.session["produtos"].get(produto_id).get("quantidade")
        )

        
        quantidade = produto.quantidade
        preco = float(produto.preco) * int(produto.quantidade)
        itempedido = ItemPedido(
            pedido=pedido, produto=produto, quantidade=quantidade, preco=preco
        )
        itempedido.save()
    
    resultado["Retorno"] = codigo_interno
    resultado["Sucesso"] = True

    return JsonResponse(resultado)
