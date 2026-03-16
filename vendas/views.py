from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pedido

class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'vendas/pedido_list.html'
    context_object_name = 'pedidos'
    paginate_by = 20
    ordering = ['-data_pedido']
    login_url = 'login'

class PedidoDetailView(LoginRequiredMixin, DetailView):
    model = Pedido
    template_name = 'vendas/pedido_detail.html'
    context_object_name = 'pedido'
    login_url = 'login'

class PedidoCreateView(LoginRequiredMixin, CreateView):
    model = Pedido
    template_name = 'vendas/pedido_form.html'
    fields = ['cliente', 'data_entrega', 'subtotal', 'desconto', 'impostos', 'total', 'status', 'observacoes']
    success_url = reverse_lazy('vendas:lista')
    login_url = 'login'

class PedidoUpdateView(LoginRequiredMixin, UpdateView):
    model = Pedido
    template_name = 'vendas/pedido_form.html'
    fields = ['cliente', 'data_entrega', 'subtotal', 'desconto', 'impostos', 'total', 'status', 'observacoes']
    success_url = reverse_lazy('vendas:lista')
    login_url = 'login'

class PedidoDeleteView(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = 'vendas/pedido_confirm_delete.html'
    success_url = reverse_lazy('vendas:lista')
    login_url = 'login'
