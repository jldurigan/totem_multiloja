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
    
class ListarIngredientes(admin.ModelAdmin):
    list_display=("id", "nome", "preco_extra", "imagem", "ativo")
    list_display_links=("id", "nome")
    list_editable=("preco_extra", "imagem", "ativo")
    search_fields=("nome", "categoria__nome")
    list_per_page=10
    
class ListarProdutos(admin.ModelAdmin):
    list_display=("id", "nome", "descricao", "preco", "imagem", "restaurante", "visivel", "ativo")
    list_display_links=("id", "nome")
    list_editable=("preco", "restaurante", "visivel", "ativo")
    search_fields=("nome", "categoria__nome", "restaurante__nome")
    list_per_page=10
    
class ListarProdutoIngredientes(admin.ModelAdmin):
    list_display=("id", "produto", "ingrediente", "quantidade_padrao", "quantidade_minima", "quantidade_maxima", "ativo")
    list_display_links=("id", "produto")
    list_editable=("ingrediente", "quantidade_padrao", "quantidade_minima", "quantidade_maxima", "ativo")
    search_fields=("nome", "produto__nome", "ingrediente__nome")
    list_per_page=10
    
class ListarCombos(admin.ModelAdmin):
    list_display=("id", "nome", "descricao", "preco", "imagem", "restaurante", "ativo")
    list_display_links=("id", "nome")
    list_editable=("descricao", "preco", "imagem", "restaurante", "ativo")
    search_fields=("nome", "produto__nome", "categoria__nome", "restaurante__nome")
    list_per_page=10
    
class ListarComboProdutos(admin.ModelAdmin):
    list_display=("id", "combo", "produto", "quantidade", "alternativa", "principal", "ativo")
    list_display_links=("id", "combo")
    list_editable=("produto", "quantidade", "alternativa", "principal", "ativo")
    search_fields=("nome", "combo__nome")
    list_per_page=10
    
class ListarPedidos(admin.ModelAdmin):
    list_display=("id", "codigo_interno", "restaurante", "nome_cliente", "total", "observacoes", "data_hora_criacao", "ativo")
    list_display_links=("id", "codigo_interno")
    search_fields=("id", "codigo_interno", "restaurante__nome")
    list_per_page=10
    
class ListarItemPedidos(admin.ModelAdmin):
    list_display=("id", "pedido", "produto", "combo", "quantidade", "preco", "ativo")
    list_display_links=("id", "pedido")
    search_fields=("pedido__codigo_interno", "produto__nome", "combo__nome")
    list_per_page=10
    
class ListarItemAlteracoes(admin.ModelAdmin):
    list_display=("id", "item", "ingrediente", "quantidade_alterada", "ativo")
    list_display_links=("id", "item")
    search_fields=("pedido__codigo_interno", "ingrediente__nome")
    list_per_page=10

admin.site.register(Restaurante, ListarRestaurantes)
admin.site.register(Categoria, ListarCategorias)
admin.site.register(Ingrediente, ListarIngredientes)
admin.site.register(Produto, ListarProdutos)
admin.site.register(ProdutoIngrediente, ListarProdutoIngredientes)
admin.site.register(Combo, ListarCombos)
admin.site.register(ComboProduto, ListarComboProdutos)
admin.site.register(Pedido, ListarPedidos)
admin.site.register(ItemPedido, ListarItemPedidos)
admin.site.register(ItemAlteracao, ListarItemAlteracoes)