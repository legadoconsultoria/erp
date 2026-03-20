from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class CategoriaInsumo(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Categoria de Insumo"
        verbose_name_plural = "Categorias de Insumo"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Insumo(models.Model):
    UNIDADE_CHOICES = [
        ('UN', 'Unidade'),
        ('CX', 'Caixa'),
        ('KG', 'Quilograma'),
        ('MT', 'Metro'),
        ('ML', 'Mililitro'),
        ('LT', 'Litro'),
        ('PC', 'Peça'),
        ('DZ', 'Dúzia'),
        ('RM', 'Resma'),
    ]
    
    STATUS_CHOICES = [
        ('AT', 'Ativo'),
        ('IN', 'Inativo'),
        ('DE', 'Descontinuado'),
    ]
    
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)
    categoria = models.ForeignKey(CategoriaInsumo, on_delete=models.PROTECT, related_name='insumos')
    descricao = models.TextField(blank=True)
    
    # Informações de quantidade
    quantidade_disponivel = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    quantidade_minima = models.IntegerField(default=10, validators=[MinValueValidator(0)])
    quantidade_maxima = models.IntegerField(default=100, validators=[MinValueValidator(0)])
    
    # Unidade de medida
    unidade = models.CharField(max_length=2, choices=UNIDADE_CHOICES, default='UN')
    
    # Preço e custo
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    custo_total = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    
    # Informações de local
    localizacao = models.CharField(max_length=100, help_text="Ex: Prateleira A-01")
    
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AT')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"
        ordering = ['categoria', 'nome']
    
    def __str__(self):
        return f"{self.nome} ({self.codigo})"


class RequisicaoMaterial(models.Model):
    STATUS_CHOICES = [
        ('PE', 'Pendente'),
        ('AP', 'Aprovada'),
        ('RE', 'Recusada'),
        ('AT', 'Atendida'),
        ('CA', 'Cancelada'),
    ]
    
    numero = models.AutoField(primary_key=True)
    usuario_solicitante = models.ForeignKey(User, on_delete=models.PROTECT, related_name='requisicoes_material')
    departamento = models.CharField(max_length=100)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PE')
    
    data_aprovacao = models.DateTimeField(null=True, blank=True)
    usuario_aprovador = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='requisicoes_aprovadas')
    
    motivo_recusa = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Requisição de Material"
        verbose_name_plural = "Requisições de Material"
        ordering = ['-data_solicitacao']
    
    def __str__(self):
        return f"Requisição #{self.numero}"


class ItemRequisicao(models.Model):
    requisicao = models.ForeignKey(RequisicaoMaterial, on_delete=models.CASCADE, related_name='itens')
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT)
    quantidade_solicitada = models.IntegerField(validators=[MinValueValidator(1)])
    quantidade_atendida = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    class Meta:
        verbose_name = "Item de Requisição"
        verbose_name_plural = "Itens de Requisição"
    
    def __str__(self):
        return f"{self.insumo.nome} x{self.quantidade_solicitada}"


class EntradaMaterial(models.Model):
    numero = models.AutoField(primary_key=True)
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT, related_name='entradas')
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    data_entrada = models.DateTimeField(auto_now_add=True)
    
    fornecedor = models.CharField(max_length=255, blank=True)
    numero_nf = models.CharField(max_length=20, blank=True)
    
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    custo_total = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    
    usuario_responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    observacoes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Entrada de Material"
        verbose_name_plural = "Entradas de Material"
        ordering = ['-data_entrada']
    
    def __str__(self):
        return f"Entrada #{self.numero} - {self.insumo.nome}"


class HistoricoAlmoxarifado(models.Model):
    TIPO_MOVIMENTO = [
        ('EN', 'Entrada'),
        ('SA', 'Saída'),
        ('AJ', 'Ajuste'),
        ('DE', 'Devolução'),
    ]
    
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT, related_name='historicos')
    tipo_movimento = models.CharField(max_length=2, choices=TIPO_MOVIMENTO)
    quantidade = models.IntegerField()
    saldo_anterior = models.IntegerField()
    saldo_atual = models.IntegerField()
    
    data_movimento = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    motivo = models.CharField(max_length=255, blank=True)
    documento_ref = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name = "Histórico do Almoxarifado"
        verbose_name_plural = "Históricos do Almoxarifado"
        ordering = ['-data_movimento']
    
    def __str__(self):
        return f"{self.get_tipo_movimento_display()} - {self.insumo.nome}"
