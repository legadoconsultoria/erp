from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'data_criacao')
    list_filter = ('ativo', 'data_criacao')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sku', 'categoria', 'preco_venda', 'quantidade_estoque', 'status')
    list_filter = ('categoria', 'status', 'data_criacao')
    search_fields = ('nome', 'sku')
    readonly_fields = ('data_criacao', 'data_atualizacao')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'sku', 'categoria', 'descricao', 'status')
        }),
        ('Preços', {
            'fields': ('preco_custo', 'preco_venda')
        }),
        ('Estoque', {
            'fields': ('quantidade_estoque', 'quantidade_minima')
        }),
        ('Impostos', {
            'fields': ('icms_aliquota', 'ipi_aliquota')
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
