from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Insumo, RequisicaoMaterial, EntradaMaterial, HistoricoAlmoxarifado

class InsumoListView(LoginRequiredMixin, ListView):
    model = Insumo
    template_name = 'almoxerifado/insumo_list.html'
    context_object_name = 'insumos'
    paginate_by = 20
    login_url = 'login'

class InsumoDetailView(LoginRequiredMixin, DetailView):
    model = Insumo
    template_name = 'almoxerifado/insumo_detail.html'
    context_object_name = 'insumo'
    login_url = 'login'

class InsumoCreateView(LoginRequiredMixin, CreateView):
    model = Insumo
    template_name = 'almoxerifado/insumo_form.html'
    fields = ['nome', 'codigo', 'categoria', 'descricao', 'quantidade_disponivel', 
              'quantidade_minima', 'quantidade_maxima', 'unidade', 'preco_unitario', 
              'custo_total', 'localizacao', 'status']
    success_url = reverse_lazy('almoxerifado:lista_insumos')
    login_url = 'login'

class InsumoUpdateView(LoginRequiredMixin, UpdateView):
    model = Insumo
    template_name = 'almoxerifado/insumo_form.html'
    fields = ['nome', 'codigo', 'categoria', 'descricao', 'quantidade_disponivel', 
              'quantidade_minima', 'quantidade_maxima', 'unidade', 'preco_unitario', 
              'custo_total', 'localizacao', 'status']
    success_url = reverse_lazy('almoxerifado:lista_insumos')
    login_url = 'login'

class InsumoDeleteView(LoginRequiredMixin, DeleteView):
    model = Insumo
    template_name = 'almoxerifado/insumo_confirm_delete.html'
    success_url = reverse_lazy('almoxerifado:lista_insumos')
    login_url = 'login'

class RequisicaoListView(LoginRequiredMixin, ListView):
    model = RequisicaoMaterial
    template_name = 'almoxerifado/requisicao_list.html'
    context_object_name = 'requisicoes'
    paginate_by = 20
    ordering = ['-data_solicitacao']
    login_url = 'login'

class RequisicaoDetailView(LoginRequiredMixin, DetailView):
    model = RequisicaoMaterial
    template_name = 'almoxerifado/requisicao_detail.html'
    context_object_name = 'requisicao'
    login_url = 'login'

class RequisicaoCreateView(LoginRequiredMixin, CreateView):
    model = RequisicaoMaterial
    template_name = 'almoxerifado/requisicao_form.html'
    fields = ['departamento', 'descricao']
    success_url = reverse_lazy('almoxerifado:lista_requisicoes')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.usuario_solicitante = self.request.user
        return super().form_valid(form)

class EntradaMaterialListView(LoginRequiredMixin, ListView):
    model = EntradaMaterial
    template_name = 'almoxerifado/entrada_list.html'
    context_object_name = 'entradas'
    paginate_by = 20
    ordering = ['-data_entrada']
    login_url = 'login'

class EntradaMaterialCreateView(LoginRequiredMixin, CreateView):
    model = EntradaMaterial
    template_name = 'almoxerifado/entrada_form.html'
    fields = ['insumo', 'quantidade', 'fornecedor', 'numero_nf', 'preco_unitario', 'custo_total', 'observacoes']
    success_url = reverse_lazy('almoxerifado:lista_entradas')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.usuario_responsavel = self.request.user
        return super().form_valid(form)

class HistoricoListView(LoginRequiredMixin, ListView):
    model = HistoricoAlmoxarifado
    template_name = 'almoxerifado/historico_list.html'
    context_object_name = 'historicos'
    paginate_by = 30
    ordering = ['-data_movimento']
    login_url = 'login'
