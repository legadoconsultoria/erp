from django.db import models
from django.core.validators import MinValueValidator

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Produto(models.Model):
    STATUS_CHOICES = [
        ('AT', 'Ativo'),
        ('IN', 'Inativo'),
        ('DE', 'Descontinuado'),
    ]
    
    nome = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos')
    descricao = models.TextField(blank=True)
    
    # Preços
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    # Estoque
    quantidade_estoque = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    quantidade_minima = models.IntegerField(default=10, validators=[MinValueValidator(0)])
    
    # Impostos
    icms_aliquota = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    ipi_aliquota = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AT')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']
    
    def __str__(self):
        return f"{self.nome} ({self.sku})"
    
    def margem_lucro(self):
        if self.preco_custo <= 0:
            return 0
        return ((self.preco_venda - self.preco_custo) / self.preco_custo) * 100
