from django.contrib import admin
from .models import *

class ListarRestaurantes(admin.ModelAdmin):
    list_display=("id", "nome", "imagem", "ativo")
    list_display_links=("id", "nome")
    list_editable=("imagem", "ativo")
    search_fields=("nome",)
    list_per_page=10
    
class ListarCategorias(admin.ModelAdmin):
    list_display=("id", "nome", "imagem", "restaurante", "visivel", "ativo")
    list_display_links=("id", "nome")
    list_editable=("imagem", "restaurante", "visivel", "ativo")
    search_fields=("nome",)
    list_per_page=10
    
class ListarProdutos(admin.ModelAdmin):
    list_display=("id", "nome", "preco", "imagem", "restaurante", "visivel", "ativo")
    list_display_links=("id", "nome")
    list_editable=("preco", "restaurante", "visivel", "ativo")
    search_fields=("nome", "categoria", "restaurante")
    list_per_page=10
    
class ListarProdutoParteProdutos(admin.ModelAdmin):
    list_display=("id", "produto_pai", "produto_parte", "quantidade", "padrao", "ativo")
    list_display_links=("id", "produto_pai")
    list_editable=("produto_parte", "quantidade", "padrao", "ativo")
    search_fields=("nome", "produto_pai")
    list_per_page=10
    
class ListarPedidos(admin.ModelAdmin):
    list_display=("id", "codigo_interno", "restaurante", "nome_cliente", "total", "observacoes", "data_hora_criacao", "ativo")
    list_display_links=("id", "codigo_interno")
    search_fields=("id", "codigo_interno", "restaurante")
    list_per_page=10
    
class ListarItemPedidos(admin.ModelAdmin):
    list_display=("id", "pedido", "produto", "quantidade", "preco", "observacoes", "ativo")
    list_display_links=("id", "pedido")
    search_fields=("produto", "produto")
    list_per_page=10

admin.site.register(Restaurante, ListarRestaurantes)
admin.site.register(Categoria, ListarCategorias)
admin.site.register(Produto, ListarProdutos)
admin.site.register(ProdutoParteProduto, ListarProdutoParteProdutos)
admin.site.register(Pedido, ListarPedidos)
admin.site.register(ItemPedido, ListarItemPedidos)