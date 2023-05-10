from django.db import models
  
class Restaurante(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False)
    logo = models.ImageField(upload_to="imagens/%Y/%m/%d/", blank=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="imagens/%Y/%m/%d/", blank=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    pedido_restaurante = models.CharField(max_length=10, null=False, blank=False, default="000")
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.restaurante.nome

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.produto.nome