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
    search_fields=("nome", "categoria")
    list_per_page=10
    
class ListarProdutos(admin.ModelAdmin):
    list_display=("id", "nome", "descricao", "preco", "imagem", "restaurante", "visivel", "ativo")
    list_display_links=("id", "nome")
    list_editable=("descricao", "preco", "restaurante", "visivel", "ativo")
    search_fields=("nome", "categoria", "restaurante")
    list_per_page=10
    
class ListarProdutoIngredientes(admin.ModelAdmin):
    list_display=("id", "produto", "ingrediente", "quantidade", "padrao", "ativo")
    list_display_links=("id", "produto")
    list_editable=("ingrediente", "quantidade", "padrao", "ativo")
    search_fields=("nome", "produto", "ingrediente")
    list_per_page=10
    
class ListarCombos(admin.ModelAdmin):
    list_display=("id", "nome", "descricao", "preco", "imagem", "restaurante", "ativo")
    list_display_links=("id", "nome")
    list_editable=("descricao", "preco", "imagem", "restaurante", "ativo")
    search_fields=("nome", "produto", "categoria", "restaurante")
    list_per_page=10
    
class ListarComboProdutos(admin.ModelAdmin):
    list_display=("id", "combo", "produto", "quantidade", "padrao", "ativo")
    list_display_links=("id", "combo")
    list_editable=("produto", "quantidade", "padrao", "ativo")
    search_fields=("nome", "combo")
    list_per_page=10
    
class ListarPedidos(admin.ModelAdmin):
    list_display=("id", "codigo_interno", "restaurante", "nome_cliente", "total", "observacoes", "data_hora_criacao", "ativo")
    list_display_links=("id", "codigo_interno")
    search_fields=("id", "codigo_interno", "restaurante")
    list_per_page=10
    
class ListarItemPedidos(admin.ModelAdmin):
    list_display=("id", "pedido", "produto", "combo", "quantidade", "preco", "observacoes", "ativo")
    list_display_links=("id", "pedido")
    search_fields=("produto", "produto", "combo")
    list_per_page=10
    
# class ListarCarrinhos(admin.ModelAdmin):
#     list_display=("id", "restaurante", "valor_total")
#     list_display_links=("id", "restaurante")
#     search_fields=("id",)
#     list_per_page=10
    
# class ListarItemCarrinhos(admin.ModelAdmin):
#     list_display=("id", "carrinho", "produto", "quantidade")
#     list_display_links=("id", "carrinho")
#     search_fields=("produto",)
#     list_per_page=10

admin.site.register(Restaurante, ListarRestaurantes)
admin.site.register(Categoria, ListarCategorias)
admin.site.register(Ingrediente, ListarIngredientes)
admin.site.register(Produto, ListarProdutos)
admin.site.register(ProdutoIngrediente, ListarProdutoIngredientes)
admin.site.register(Combo, ListarCombos)
admin.site.register(ComboProduto, ListarComboProdutos)
admin.site.register(Pedido, ListarPedidos)
admin.site.register(ItemPedido, ListarItemPedidos)
# admin.site.register(Carrinho, ListarCarrinhos)
# admin.site.register(ItemCarrinho, ListarItemCarrinhos)