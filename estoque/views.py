from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from produtos.models import Produto
from .models import MovimentacaoEstoque

class EstoqueListView(ListView):
    model = Produto
    template_name = 'estoque/estoque_list.html'
    context_object_name = 'produtos'
    paginate_by = 20

class MovimentacaoListView(ListView):
    model = MovimentacaoEstoque
    template_name = 'estoque/movimentacao_list.html'
    context_object_name = 'movimentacoes'
    paginate_by = 30
    ordering = ['-data_movimentacao']

class MovimentacaoCreateView(CreateView):
    model = MovimentacaoEstoque
    template_name = 'estoque/movimentacao_form.html'
    fields = ['produto', 'tipo', 'motivo', 'quantidade', 'saldo_anterior', 'saldo_atual', 'responsavel', 'observacoes']
    success_url = reverse_lazy('estoque:movimentacoes')
