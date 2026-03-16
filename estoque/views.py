from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from produtos.models import Produto
from .models import MovimentacaoEstoque

class EstoqueListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'estoque/estoque_list.html'
    context_object_name = 'produtos'
    paginate_by = 20
    login_url = 'login'

class MovimentacaoListView(LoginRequiredMixin, ListView):
    model = MovimentacaoEstoque
    template_name = 'estoque/movimentacao_list.html'
    context_object_name = 'movimentacoes'
    paginate_by = 30
    ordering = ['-data_movimentacao']
    login_url = 'login'

class MovimentacaoCreateView(LoginRequiredMixin, CreateView):
    model = MovimentacaoEstoque
    template_name = 'estoque/movimentacao_form.html'
    fields = ['produto', 'tipo', 'motivo', 'quantidade', 'saldo_anterior', 'saldo_atual', 'responsavel', 'observacoes']
    success_url = reverse_lazy('estoque:movimentacoes')
    login_url = 'login'
