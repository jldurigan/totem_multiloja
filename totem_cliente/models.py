from django.db import models

class Anexo(models.Model):
    nome = models.CharField(max_length=30)
    caminho = models.CharField(max_length=200)
    ativo = models.BooleanField
    
    def __str__(self) -> str:
        return self.caminho
    
class Restaurante(models.Model):
    nome = models.CharField(max_length=40)
    anexo = models.ManyToManyField(Anexo)
    ativo = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=40)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    anexo = models.ManyToManyField(Anexo)
    ativo = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.nome
    
class Pedido(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2)
    ativo = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.restaurante.nome

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    ativo = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.produto.nome