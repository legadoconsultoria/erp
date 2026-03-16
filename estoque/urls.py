from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.EstoqueListView.as_view(), name='lista'),
    path('movimentacoes/', views.MovimentacaoListView.as_view(), name='movimentacoes'),
    path('movimentacoes/criar/', views.MovimentacaoCreateView.as_view(), name='criar_movimentacao'),
]
