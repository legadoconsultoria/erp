from django.db import models
from django.core.validators import MinValueValidator
from produtos.models import Produto

class Fornecedor(models.Model):
    STATUS_CHOICES = [
        ('AT', 'Ativo'),
        ('IN', 'Inativo'),
        ('BL', 'Bloqueado'),
    ]
    
    nome = models.CharField(max_length=255, unique=True)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    
    # Endereço
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    
    # Informações comerciais
    prazo_pagamento = models.IntegerField(default=30)  # dias
    limite_credito = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AT')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class OrdenCompra(models.Model):
    STATUS_CHOICES = [
        ('RH', 'Rascunho'),
        ('EM', 'Emitida'),
        ('PR', 'Recebida Parcialmente'),
        ('RC', 'Recebida Totalmente'),
        ('CN', 'Cancelada'),
    ]
    
    numero = models.AutoField(primary_key=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name='ordens_compra')
    data_emissao = models.DateTimeField(auto_now_add=True)
    data_entrega_prevista = models.DateField()
    
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    impostos = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    frete = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RH')
    observacoes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Ordem de Compra"
        verbose_name_plural = "Ordens de Compra"
        ordering = ['-data_emissao']
    
    def __str__(self):
        return f"OC #{self.numero}"


class ItemOrdenCompra(models.Model):
    ordem_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    
    class Meta:
        verbose_name = "Item da Ordem de Compra"
        verbose_name_plural = "Itens da Ordem de Compra"
    
    def __str__(self):
        return f"{self.produto.nome} x{self.quantidade}"
