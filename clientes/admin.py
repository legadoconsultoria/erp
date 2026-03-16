from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'cpf_cnpj', 'email', 'telefone', 'status', 'data_cadastro')
    list_filter = ('tipo', 'status', 'data_cadastro')
    search_fields = ('nome', 'cpf_cnpj', 'email')
    readonly_fields = ('data_cadastro', 'data_atualizacao')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'tipo', 'cpf_cnpj', 'email', 'telefone', 'status')
        }),
        ('Endereço', {
            'fields': ('endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep')
        }),
        ('Informações Comerciais', {
            'fields': ('limite_credito', 'desconto_padrao')
        }),
        ('Datas', {
            'fields': ('data_cadastro', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
