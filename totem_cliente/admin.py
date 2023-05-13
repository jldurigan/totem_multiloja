from django.contrib import admin
from .models import *

class ListarRestaurantes(admin.ModelAdmin):
    list_display=("id", "nome", "logo", "ativo")
    list_display_links=("id", "nome")
    list_editable=("ativo",)
    search_fields=("nome",)
    list_per_page=10
    
class ListarProdutos(admin.ModelAdmin):
    list_display=("id", "nome", "valor", "imagem", "restaurante", "ativo")
    list_display_links=("id", "nome")
    list_editable=("valor", "restaurante", "ativo")
    search_fields=("nome",)
    list_per_page=10
    
class ListarPedidos(admin.ModelAdmin):
    list_display=("id", "pedido_restaurante", "restaurante", "valor_total", "ativo")
    list_display_links=("id", "pedido_restaurante")
    search_fields=("id",)
    list_per_page=10
    
class ListarItemPedidos(admin.ModelAdmin):
    list_display=("id", "pedido", "produto", "quantidade", "ativo")
    list_display_links=("id", "pedido")
    search_fields=("produto",)
    list_per_page=10
    
class ListarCarrinhos(admin.ModelAdmin):
    list_display=("id", "restaurante", "valor_total")
    list_display_links=("id", "restaurante")
    search_fields=("id",)
    list_per_page=10
    
class ListarItemCarrinhos(admin.ModelAdmin):
    list_display=("id", "carrinho", "produto", "quantidade")
    list_display_links=("id", "carrinho")
    search_fields=("produto",)
    list_per_page=10

admin.site.register(Restaurante, ListarRestaurantes)
admin.site.register(Produto, ListarProdutos)
admin.site.register(Pedido, ListarPedidos)
admin.site.register(ItemPedido, ListarItemPedidos)
admin.site.register(Carrinho, ListarCarrinhos)
admin.site.register(ItemCarrinho, ListarItemCarrinhos)