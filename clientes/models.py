from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cliente(models.Model):
    TIPO_CLIENTE = [
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    ]
    
    STATUS_CHOICES = [
        ('AT', 'Ativo'),
        ('IN', 'Inativo'),
        ('SU', 'Suspenso'),
    ]
    
    nome = models.CharField(max_length=255, unique=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CLIENTE, default='F')
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
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
    limite_credito = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    desconto_padrao = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AT')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome']
    
    def __str__(self):
        return f"{self.nome} ({self.cpf_cnpj})"
