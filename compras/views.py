from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Fornecedor, OrdenCompra

class FornecedorListView(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'compras/fornecedor_list.html'
    context_object_name = 'fornecedores'
    paginate_by = 20
    login_url = 'login'

class FornecedorDetailView(LoginRequiredMixin, DetailView):
    model = Fornecedor
    template_name = 'compras/fornecedor_detail.html'
    context_object_name = 'fornecedor'
    login_url = 'login'

class FornecedorCreateView(LoginRequiredMixin, CreateView):
    model = Fornecedor
    template_name = 'compras/fornecedor_form.html'
    fields = ['nome', 'cnpj', 'email', 'telefone', 'endereco', 'numero', 'complemento', 
              'bairro', 'cidade', 'estado', 'cep', 'prazo_pagamento', 'limite_credito', 'status']
    success_url = reverse_lazy('compras:lista_fornecedores')
    login_url = 'login'

class FornecedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    template_name = 'compras/fornecedor_form.html'
    fields = ['nome', 'cnpj', 'email', 'telefone', 'endereco', 'numero', 'complemento', 
              'bairro', 'cidade', 'estado', 'cep', 'prazo_pagamento', 'limite_credito', 'status']
    success_url = reverse_lazy('compras:lista_fornecedores')
    login_url = 'login'

class FornecedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = 'compras/fornecedor_confirm_delete.html'
    success_url = reverse_lazy('compras:lista_fornecedores')
    login_url = 'login'

class OrdenCompraListView(LoginRequiredMixin, ListView):
    model = OrdenCompra
    template_name = 'compras/ordencompra_list.html'
    context_object_name = 'ordens'
    paginate_by = 20
    ordering = ['-data_emissao']
    login_url = 'login'

class OrdenCompraDetailView(LoginRequiredMixin, DetailView):
    model = OrdenCompra
    template_name = 'compras/ordencompra_detail.html'
    context_object_name = 'ordem'
    login_url = 'login'

class OrdenCompraCreateView(LoginRequiredMixin, CreateView):
    model = OrdenCompra
    template_name = 'compras/ordencompra_form.html'
    fields = ['fornecedor', 'data_entrega_prevista', 'subtotal', 'impostos', 'frete', 'total', 'status', 'observacoes']
    success_url = reverse_lazy('compras:lista_ordens')
    login_url = 'login'

class OrdenCompraUpdateView(LoginRequiredMixin, UpdateView):
    model = OrdenCompra
    template_name = 'compras/ordencompra_form.html'
    fields = ['fornecedor', 'data_entrega_prevista', 'subtotal', 'impostos', 'frete', 'total', 'status', 'observacoes']
    success_url = reverse_lazy('compras:lista_ordens')
    login_url = 'login'

class OrdenCompraDeleteView(LoginRequiredMixin, DeleteView):
    model = OrdenCompra
    template_name = 'compras/ordencompra_confirm_delete.html'
    success_url = reverse_lazy('compras:lista_ordens')
    login_url = 'login'
