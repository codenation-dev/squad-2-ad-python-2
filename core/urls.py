"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers
from planos.views import PlanosViewSet
from vendedores.views import VendedoresViewSet, ComissoesViewSet
from vendas.views import VendasViewSet
from vendas.views import notificar_vendedores

router = routers.DefaultRouter()
router.register(r"plano", PlanosViewSet)
router.register(r"vendedor", VendedoresViewSet)
router.register(r"venda", VendasViewSet, base_name='venda')
router.register(r"comissoes/(?P<mes>[0-9]+)", viewset=ComissoesViewSet, base_name='comissoes')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/checar_comissao/", notificar_vendedores),
]
