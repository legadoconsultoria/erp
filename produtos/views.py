from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Produto

class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produtos/produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 20
    login_url = 'login'

class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = 'produtos/produto_detail.html'
    context_object_name = 'produto'
    login_url = 'login'

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'produtos/produto_form.html'
    fields = ['nome', 'sku', 'categoria', 'descricao', 'preco_custo', 'preco_venda', 
              'quantidade_estoque', 'quantidade_minima', 'icms_aliquota', 'ipi_aliquota', 'status']
    success_url = reverse_lazy('produtos:lista')
    login_url = 'login'

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = 'produtos/produto_form.html'
    fields = ['nome', 'sku', 'categoria', 'descricao', 'preco_custo', 'preco_venda', 
              'quantidade_estoque', 'quantidade_minima', 'icms_aliquota', 'ipi_aliquota', 'status']
    success_url = reverse_lazy('produtos:lista')
    login_url = 'login'

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produtos/produto_confirm_delete.html'
    success_url = reverse_lazy('produtos:lista')
    login_url = 'login'
