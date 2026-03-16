from django.db import models
from django.core.validators import MinValueValidator
from produtos.models import Produto

class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = [
        ('EN', 'Entrada'),
        ('SA', 'Saída'),
        ('AD', 'Ajuste'),
    ]
    
    MOTIVO_CHOICES = [
        ('CO', 'Compra'),
        ('DEV', 'Devolução'),
        ('VD', 'Venda'),
        ('AJ', 'Ajuste'),
        ('QM', 'Quebra/Máquina'),
        ('OU', 'Outro'),
    ]
    
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='movimentacoes')
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    motivo = models.CharField(max_length=3, choices=MOTIVO_CHOICES)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    saldo_anterior = models.IntegerField()
    saldo_atual = models.IntegerField()
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    responsavel = models.CharField(max_length=100, blank=True)
    observacoes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Movimentação de Estoque"
        verbose_name_plural = "Movimentações de Estoque"
        ordering = ['-data_movimentacao']
    
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.produto.nome} ({self.quantidade})"


class InventarioEstoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, primary_key=True, related_name='inventario')
    quantidade_sistema = models.IntegerField(default=0)
    quantidade_fisica = models.IntegerField(default=0)
    diferenca = models.IntegerField(default=0)
    data_ultima_contagem = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('OK', 'Ok'), ('DIV', 'Divergência')])
    
    class Meta:
        verbose_name = "Inventário de Estoque"
        verbose_name_plural = "Inventários de Estoque"
    
    def __str__(self):
        return f"Inv. {self.produto.nome}"
