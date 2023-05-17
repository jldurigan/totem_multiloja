from django.contrib import admin
from .models import *

class ListarRestaurantes(admin.ModelAdmin):
    list_display=("id", "nome", "imagem", "ativo")
    list_display_links=("id", "nome")
    list_editable=("imagem", "ativo")
    search_fields=("nome",)
    list_per_page=10
    
class ListarCategorias(admin.ModelAdmin):
    list_display=("id", "nome", "imagem", "restaurante", "ativo")
    list_display_links=("id", "nome")
    list_editable=("imagem", "restaurante", "ativo")
    search_fields=("nome",)
    list_per_page=10
    
class ListarProdutos(admin.ModelAdmin):
    list_display=("id", "nome", "descricao", "preco", "imagem", "restaurante", "ativo")
    list_display_links=("id", "nome")
    list_editable=("preco", "restaurante", "ativo")
    search_fields=("nome", "categoria__nome", "restaurante__nome")
    list_per_page=10
    
class ListarPedidos(admin.ModelAdmin):
    list_display=("id", "codigo_interno", "restaurante", "nome_cliente", "total", "observacoes", "data_hora_criacao", "ativo")
    list_display_links=("id", "codigo_interno")
    search_fields=("id", "codigo_interno", "restaurante__nome")
    list_per_page=10
    
class ListarItemPedidos(admin.ModelAdmin):
    list_display=("id", "pedido", "produto", "quantidade", "preco", "ativo")
    list_display_links=("id", "pedido")
    search_fields=("pedido__codigo_interno", "produto__nome")
    list_per_page=10

admin.site.register(Restaurante, ListarRestaurantes)
admin.site.register(Categoria, ListarCategorias)
admin.site.register(Produto, ListarProdutos)
admin.site.register(Pedido, ListarPedidos)
admin.site.register(ItemPedido, ListarItemPedidos)