from django.urls import path
from . import views

app_name = 'vendas'

urlpatterns = [
    path('', views.PedidoListView.as_view(), name='lista'),
    path('criar/', views.PedidoCreateView.as_view(), name='criar'),
    path('<int:pk>/', views.PedidoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', views.PedidoUpdateView.as_view(), name='editar'),
    path('<int:pk>/deletar/', views.PedidoDeleteView.as_view(), name='deletar'),
]
