from django.contrib import admin
from .models import CategoriaInsumo, Insumo, RequisicaoMaterial, ItemRequisicao, EntradaMaterial, HistoricoAlmoxarifado

@admin.register(CategoriaInsumo)
class CategoriaInsumoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'data_criacao')
    list_filter = ('ativo', 'data_criacao')
    search_fields = ('nome',)

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'categoria', 'quantidade_disponivel', 'quantidade_minima', 'status', 'localizacao')
    list_filter = ('categoria', 'status', 'unidade')
    search_fields = ('nome', 'codigo')
    readonly_fields = ('data_criacao', 'data_atualizacao')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'codigo', 'categoria', 'descricao', 'status')
        }),
        ('Quantidade', {
            'fields': ('quantidade_disponivel', 'quantidade_minima', 'quantidade_maxima', 'unidade')
        }),
        ('Preço e Custo', {
            'fields': ('preco_unitario', 'custo_total')
        }),
        ('Localização', {
            'fields': ('localizacao',)
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

class ItemRequisicaoInline(admin.TabularInline):
    model = ItemRequisicao
    extra = 1

@admin.register(RequisicaoMaterial)
class RequisicaoMaterialAdmin(admin.ModelAdmin):
    list_display = ('numero', 'usuario_solicitante', 'departamento', 'data_solicitacao', 'status')
    list_filter = ('status', 'data_solicitacao', 'departamento')
    search_fields = ('numero', 'usuario_solicitante__username', 'departamento')
    readonly_fields = ('data_solicitacao', 'numero')
    inlines = [ItemRequisicaoInline]
    
    fieldsets = (
        ('Informações da Requisição', {
            'fields': ('numero', 'usuario_solicitante', 'departamento', 'data_solicitacao')
        }),
        ('Status', {
            'fields': ('status', 'usuario_aprovador', 'data_aprovacao')
        }),
        ('Descrição', {
            'fields': ('descricao',)
        }),
        ('Motivo de Recusa', {
            'fields': ('motivo_recusa',),
            'classes': ('collapse',)
        }),
    )

@admin.register(EntradaMaterial)
class EntradaMaterialAdmin(admin.ModelAdmin):
    list_display = ('numero', 'insumo', 'quantidade', 'data_entrada', 'fornecedor', 'custo_total')
    list_filter = ('data_entrada', 'insumo__categoria')
    search_fields = ('insumo__nome', 'fornecedor', 'numero_nf')
    readonly_fields = ('data_entrada', 'numero')
    date_hierarchy = 'data_entrada'

@admin.register(HistoricoAlmoxarifado)
class HistoricoAlmoxarifadoAdmin(admin.ModelAdmin):
    list_display = ('insumo', 'tipo_movimento', 'quantidade', 'saldo_anterior', 'saldo_atual', 'data_movimento', 'usuario')
    list_filter = ('tipo_movimento', 'data_movimento')
    search_fields = ('insumo__nome', 'usuario__username')
    readonly_fields = ('data_movimento', 'insumo', 'quantidade', 'saldo_anterior', 'saldo_atual')
    date_hierarchy = 'data_movimento'
