from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Fornecedor, OrdenCompra

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'compras/fornecedor_list.html'
    context_object_name = 'fornecedores'
    paginate_by = 20

class FornecedorDetailView(DetailView):
    model = Fornecedor
    template_name = 'compras/fornecedor_detail.html'
    context_object_name = 'fornecedor'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    template_name = 'compras/fornecedor_form.html'
    fields = ['nome', 'cnpj', 'email', 'telefone', 'endereco', 'numero', 'complemento', 
              'bairro', 'cidade', 'estado', 'cep', 'prazo_pagamento', 'limite_credito', 'status']
    success_url = reverse_lazy('compras:lista_fornecedores')

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    template_name = 'compras/fornecedor_form.html'
    fields = ['nome', 'cnpj', 'email', 'telefone', 'endereco', 'numero', 'complemento', 
              'bairro', 'cidade', 'estado', 'cep', 'prazo_pagamento', 'limite_credito', 'status']
    success_url = reverse_lazy('compras:lista_fornecedores')

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = 'compras/fornecedor_confirm_delete.html'
    success_url = reverse_lazy('compras:lista_fornecedores')

class OrdenCompraListView(ListView):
    model = OrdenCompra
    template_name = 'compras/ordencompra_list.html'
    context_object_name = 'ordens'
    paginate_by = 20
    ordering = ['-data_emissao']

class OrdenCompraDetailView(DetailView):
    model = OrdenCompra
    template_name = 'compras/ordencompra_detail.html'
    context_object_name = 'ordem'

class OrdenCompraCreateView(CreateView):
    model = OrdenCompra
    template_name = 'compras/ordencompra_form.html'
    fields = ['fornecedor', 'data_entrega_prevista', 'subtotal', 'impostos', 'frete', 'total', 'status', 'observacoes']
    success_url = reverse_lazy('compras:lista_ordens')

class OrdenCompraUpdateView(UpdateView):
    model = OrdenCompra
    template_name = 'compras/ordencompra_form.html'
    fields = ['fornecedor', 'data_entrega_prevista', 'subtotal', 'impostos', 'frete', 'total', 'status', 'observacoes']
    success_url = reverse_lazy('compras:lista_ordens')

class OrdenCompraDeleteView(DeleteView):
    model = OrdenCompra
    template_name = 'compras/ordencompra_confirm_delete.html'
    success_url = reverse_lazy('compras:lista_ordens')
