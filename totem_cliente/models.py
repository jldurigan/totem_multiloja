from django.db import models

class Restaurante(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False)
    imagem = models.ImageField(upload_to='imagens/restaurantes/%Y/%m/%d/', blank=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False)
    imagem = models.ImageField(upload_to='imagens/categorias/%Y/%m/%d/', blank=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False)
    descricao = models.TextField(max_length=500, blank=False, null=False)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    imagem = models.ImageField(upload_to='imagens/produtos/%Y/%m/%d/', blank=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)    
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome


class Pedido(models.Model):
    codigo_interno = models.CharField(max_length=10, null=False, blank=False)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=100, null=False, blank=False)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    observacoes = models.TextField(blank=True)
    data_hora_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.restaurante.nome} - Pedido {self.codigo_interno}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.pedido.restaurante.nome} Pedido {self.pedido.codigo_interno} Item {self.id}"
    
