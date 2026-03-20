"""
URL configuration for core_erp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('modulos/', views.modulos_view, name='modulos'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('api/dashboard/', views.dashboard_api, name='dashboard_api'),
    path('admin/', admin.site.urls),
    
    # ERP URLs
    path('clientes/', include('clientes.urls')),
    path('produtos/', include('produtos.urls')),
    path('vendas/', include('vendas.urls')),
    path('compras/', include('compras.urls')),
    path('estoque/', include('estoque.urls')),
    path('almoxerifado/', include('almoxerifado.urls')),
]
