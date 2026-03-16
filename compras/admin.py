from django.contrib import admin
from .models import Fornecedor, OrdenCompra, ItemOrdenCompra

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'email', 'telefone', 'status')
    list_filter = ('status', 'data_cadastro')
    search_fields = ('nome', 'cnpj', 'email')
    readonly_fields = ('data_cadastro',)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'cnpj', 'email', 'telefone', 'status')
        }),
        ('Endereço', {
            'fields': ('endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep')
        }),
        ('Informações Comerciais', {
            'fields': ('prazo_pagamento', 'limite_credito')
        }),
    )

class ItemOrdenCompraInline(admin.TabularInline):
    model = ItemOrdenCompra
    extra = 1

@admin.register(OrdenCompra)
class OrdenCompraAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fornecedor', 'data_emissao', 'total', 'status')
    list_filter = ('status', 'data_emissao')
    search_fields = ('numero', 'fornecedor__nome')
    readonly_fields = ('data_emissao',)
    inlines = [ItemOrdenCompraInline]
    
    fieldsets = (
        ('Informações da Ordem', {
            'fields': ('numero', 'fornecedor', 'data_emissao', 'data_entrega_prevista', 'status')
        }),
        ('Totais', {
            'fields': ('subtotal', 'impostos', 'frete', 'total')
        }),
        ('Observações', {
            'fields': ('observacoes',),
            'classes': ('collapse',)
        }),
    )
