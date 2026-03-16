from django.db import models
from django.core.validators import MinValueValidator
from clientes.models import Cliente
from produtos.models import Produto

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('RH', 'Rascunho'),
        ('EM', 'Emissão'),
        ('EF', 'Emitido'),
        ('CN', 'Cancelado'),
        ('AG', 'Aguardando Envio'),
        ('EN', 'Enviado'),
        ('NT', 'Nota Fiscal Emitida'),
    ]
    
    numero = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='pedidos')
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    desconto = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    impostos = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RH')
    observacoes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Pedido de Venda"
        verbose_name_plural = "Pedidos de Venda"
        ordering = ['-data_pedido']
    
    def __str__(self):
        return f"Pedido #{self.numero}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    desconto_item = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    
    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"
    
    def __str__(self):
        return f"{self.produto.nome} x{self.quantidade}"
