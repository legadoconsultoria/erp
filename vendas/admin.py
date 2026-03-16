from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cliente', 'data_pedido', 'total', 'status')
    list_filter = ('status', 'data_pedido')
    search_fields = ('numero', 'cliente__nome')
    readonly_fields = ('data_pedido',)
    inlines = [ItemPedidoInline]
    
    fieldsets = (
        ('Informações do Pedido', {
            'fields': ('numero', 'cliente', 'data_pedido', 'data_entrega', 'status')
        }),
        ('Totais', {
            'fields': ('subtotal', 'desconto', 'impostos', 'total')
        }),
        ('Observações', {
            'fields': ('observacoes',),
            'classes': ('collapse',)
        }),
    )
