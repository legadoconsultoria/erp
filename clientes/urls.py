from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='lista'),
    path('criar/', views.ClienteCreateView.as_view(), name='criar'),
    path('<int:pk>/', views.ClienteDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='editar'),
    path('<int:pk>/deletar/', views.ClienteDeleteView.as_view(), name='deletar'),
]
