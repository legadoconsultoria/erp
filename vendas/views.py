from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pedido

class PedidoListView(ListView):
    model = Pedido
    template_name = 'vendas/pedido_list.html'
    context_object_name = 'pedidos'
    paginate_by = 20
    ordering = ['-data_pedido']

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'vendas/pedido_detail.html'
    context_object_name = 'pedido'

class PedidoCreateView(CreateView):
    model = Pedido
    template_name = 'vendas/pedido_form.html'
    fields = ['cliente', 'data_entrega', 'subtotal', 'desconto', 'impostos', 'total', 'status', 'observacoes']
    success_url = reverse_lazy('vendas:lista')

class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = 'vendas/pedido_form.html'
    fields = ['cliente', 'data_entrega', 'subtotal', 'desconto', 'impostos', 'total', 'status', 'observacoes']
    success_url = reverse_lazy('vendas:lista')

class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'vendas/pedido_confirm_delete.html'
    success_url = reverse_lazy('vendas:lista')
