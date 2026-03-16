from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cliente

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 20
    login_url = 'login'

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'
    context_object_name = 'cliente'
    login_url = 'login'

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nome', 'tipo', 'cpf_cnpj', 'email', 'telefone', 'endereco', 'numero', 
              'complemento', 'bairro', 'cidade', 'estado', 'cep', 'limite_credito', 
              'desconto_padrao', 'status']
    success_url = reverse_lazy('clientes:lista')
    login_url = 'login'

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nome', 'tipo', 'cpf_cnpj', 'email', 'telefone', 'endereco', 'numero', 
              'complemento', 'bairro', 'cidade', 'estado', 'cep', 'limite_credito', 
              'desconto_padrao', 'status']
    success_url = reverse_lazy('clientes:lista')
    login_url = 'login'

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('clientes:lista')
    login_url = 'login'
