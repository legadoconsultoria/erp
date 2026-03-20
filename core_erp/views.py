from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import JsonResponse
from .forms import LoginForm
from clientes.models import Cliente
from produtos.models import Produto
from vendas.models import Pedido
from compras.models import Fornecedor, OrdenCompra
from estoque.models import MovimentacaoEstoque
from almoxerifado.models import Insumo, RequisicaoMaterial

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
                    'almoxerifado': 'almoxerifado:lista_insumos',
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
            'nome': 'Almoxarifado',
            'descricao': 'Gestão de insumos e requisições',
            'icon': '📋',
            'url': 'almoxerifado:lista_insumos',
            'cor': 'cyan'
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

@login_required(login_url='login')
def dashboard_view(request):
    """Dashboard com estatísticas gerais do sistema"""
    
    # Estatísticas por módulo
    stats = {
        'clientes': {
            'total': Cliente.objects.count(),
            'ativos': Cliente.objects.filter(status='ativo').count(),
            'inativos': Cliente.objects.filter(status='inativo').count(),
        },
        'produtos': {
            'total': Produto.objects.count(),
            'ativos': Produto.objects.filter(status='ativo').count(),
            'baixo_estoque': Produto.objects.filter(quantidade_estoque__lt=Produto.objects.values_list('quantidade_minima', flat=True)[0] if Produto.objects.exists() else 0).count(),
        },
        'vendas': {
            'total': Pedido.objects.count(),
            'pendentes': Pedido.objects.filter(status='PE').count(),
            'concluidas': Pedido.objects.filter(status='CO').count(),
            'valor_total': sum(p.total for p in Pedido.objects.all()),
        },
        'compras': {
            'fornecedores': Fornecedor.objects.count(),
            'ordens': OrdenCompra.objects.count(),
            'pendentes': OrdenCompra.objects.filter(status='PE').count(),
        },
        'estoque': {
            'movimentacoes': MovimentacaoEstoque.objects.count(),
            'entradas': MovimentacaoEstoque.objects.filter(tipo='EN').count(),
            'saidas': MovimentacaoEstoque.objects.filter(tipo='SA').count(),
        },
        'almoxerifado': {
            'insumos': Insumo.objects.count(),
            'requisicoes': RequisicaoMaterial.objects.count(),
            'pendentes': RequisicaoMaterial.objects.filter(status='PE').count(),
        },
    }
    
    contexto = {
        'stats': stats,
        'usuario': request.user
    }
    
    return render(request, 'core_erp/dashboard.html', contexto)

@login_required(login_url='login')
def dashboard_api(request):
    """API que retorna dados para os gráficos do dashboard"""
    from django.db.models import Sum, Count
    from datetime import datetime, timedelta
    
    # Vendas dos últimos 30 dias
    data_inicio = datetime.now() - timedelta(days=30)
    vendas_30dias = Pedido.objects.filter(data_pedido__gte=data_inicio).values('data_pedido__date').annotate(total=Sum('total')).order_by('data_pedido__date')
    
    # Movimentações de estoque
    entradas = MovimentacaoEstoque.objects.filter(tipo='EN').count()
    saidas = MovimentacaoEstoque.objects.filter(tipo='SA').count()
    
    # Produtos por categoria
    produtos_categoria = Produto.objects.values('categoria__nome').annotate(count=Count('id')).order_by('-count')[:5]
    
    dados = {
        'vendas_30dias': list(vendas_30dias),
        'movimentacoes_estoque': {
            'entradas': entradas,
            'saidas': saidas,
        },
        'produtos_categoria': list(produtos_categoria),
    }
    
    return JsonResponse(dados)
