from django.urls import path
from . import views

app_name = 'almoxerifado'

urlpatterns = [
    path('insumos/', views.InsumoListView.as_view(), name='lista_insumos'),
    path('insumos/criar/', views.InsumoCreateView.as_view(), name='criar_insumo'),
    path('insumos/<int:pk>/', views.InsumoDetailView.as_view(), name='detalhe_insumo'),
    path('insumos/<int:pk>/editar/', views.InsumoUpdateView.as_view(), name='editar_insumo'),
    path('insumos/<int:pk>/deletar/', views.InsumoDeleteView.as_view(), name='deletar_insumo'),
    
    path('requisicoes/', views.RequisicaoListView.as_view(), name='lista_requisicoes'),
    path('requisicoes/criar/', views.RequisicaoCreateView.as_view(), name='criar_requisicao'),
    path('requisicoes/<int:pk>/', views.RequisicaoDetailView.as_view(), name='detalhe_requisicao'),
    
    path('entradas/', views.EntradaMaterialListView.as_view(), name='lista_entradas'),
    path('entradas/criar/', views.EntradaMaterialCreateView.as_view(), name='criar_entrada'),
    
    path('historico/', views.HistoricoListView.as_view(), name='historico'),
]
