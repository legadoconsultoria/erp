from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .forms import LoginForm

@require_http_methods(["GET", "POST"])
def login_view(request):
    """Página de login do sistema"""
    if request.user.is_authenticated:
        return redirect('modulos')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            modulo = form.cleaned_data['modulo']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo, {user.first_name or user.username}!')
                
                # Redirecionar para o módulo selecionado
                modulo_urls = {
                    'clientes': 'clientes:lista',
                    'produtos': 'produtos:lista',
                    'vendas': 'vendas:lista',
                    'compras': 'compras:lista_fornecedores',
                    'estoque': 'estoque:lista',
                    'admin': '/admin/',
                }
                
                url = modulo_urls.get(modulo, 'modulos')
                return redirect(url)
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    
    return render(request, 'core_erp/login.html', {'form': form})

@login_required(login_url='login')
def modulos_view(request):
    """Página de seleção de módulos"""
    modulos = [
        {
            'nome': 'Clientes',
            'descricao': 'Gerenciar clientes e informações de contato',
            'icon': '👥',
            'url': 'clientes:lista',
            'cor': 'primary'
        },
        {
            'nome': 'Produtos',
            'descricao': 'Catálogo de produtos e categorias',
            'icon': '📦',
            'url': 'produtos:lista',
            'cor': 'success'
        },
        {
            'nome': 'Vendas',
            'descricao': 'Pedidos de venda e faturamento',
            'icon': '💰',
            'url': 'vendas:lista',
            'cor': 'danger'
        },
        {
            'nome': 'Compras',
            'descricao': 'Ordens de compra e fornecedores',
            'icon': '🛒',
            'url': 'compras:lista_fornecedores',
            'cor': 'warning'
        },
        {
            'nome': 'Estoque',
            'descricao': 'Controle de estoque e movimentações',
            'icon': '📊',
            'url': 'estoque:lista',
            'cor': 'info'
        },
        {
            'nome': 'Admin',
            'descricao': 'Painel administrativo do sistema',
            'icon': '⚙️',
            'url': '/admin/',
            'cor': 'secondary'
        },
    ]
    
    contexto = {
        'modulos': modulos,
        'usuario': request.user
    }
    return render(request, 'core_erp/modulos.html', contexto)

@require_http_methods(["POST"])
def logout_view(request):
    """Logout do sistema"""
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('login')
