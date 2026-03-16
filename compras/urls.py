from django.urls import path
from . import views

app_name = 'compras'

urlpatterns = [
    path('fornecedores/', views.FornecedorListView.as_view(), name='lista_fornecedores'),
    path('fornecedores/criar/', views.FornecedorCreateView.as_view(), name='criar_fornecedor'),
    path('fornecedores/<int:pk>/', views.FornecedorDetailView.as_view(), name='detalhe_fornecedor'),
    path('fornecedores/<int:pk>/editar/', views.FornecedorUpdateView.as_view(), name='editar_fornecedor'),
    path('fornecedores/<int:pk>/deletar/', views.FornecedorDeleteView.as_view(), name='deletar_fornecedor'),
    
    path('ordens/', views.OrdenCompraListView.as_view(), name='lista_ordens'),
    path('ordens/criar/', views.OrdenCompraCreateView.as_view(), name='criar_ordem'),
    path('ordens/<int:pk>/', views.OrdenCompraDetailView.as_view(), name='detalhe_ordem'),
    path('ordens/<int:pk>/editar/', views.OrdenCompraUpdateView.as_view(), name='editar_ordem'),
    path('ordens/<int:pk>/deletar/', views.OrdenCompraDeleteView.as_view(), name='deletar_ordem'),
]
