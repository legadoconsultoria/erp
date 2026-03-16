from django.contrib import admin
from .models import MovimentacaoEstoque, InventarioEstoque

@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'motivo', 'quantidade', 'saldo_anterior', 'saldo_atual', 'data_movimentacao')
    list_filter = ('tipo', 'motivo', 'data_movimentacao')
    search_fields = ('produto__nome', 'responsavel')
    readonly_fields = ('data_movimentacao',)
    date_hierarchy = 'data_movimentacao'

@admin.register(InventarioEstoque)
class InventarioEstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade_sistema', 'quantidade_fisica', 'diferenca', 'status')
    list_filter = ('status', 'data_ultima_contagem')
    search_fields = ('produto__nome',)
    readonly_fields = ('data_ultima_contagem', 'produto')
