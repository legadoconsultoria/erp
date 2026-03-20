from django import forms
from django.contrib.auth.models import User

MODULOS_CHOICES = [
    ('clientes', '👥 Clientes'),
    ('produtos', '📦 Produtos'),
    ('vendas', '💰 Vendas'),
    ('compras', '🛒 Compras'),
    ('estoque', '📊 Estoque'),
    ('almoxerifado', '📋 Almoxarifado'),
    ('admin', '⚙️ Admin'),
]

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu usuário',
            'autofocus': True
        })
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )
    modulo = forms.ChoiceField(
        label='Selecione o Módulo',
        choices=MODULOS_CHOICES,
        initial='clientes',
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
