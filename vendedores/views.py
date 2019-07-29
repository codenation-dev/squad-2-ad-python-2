from django.shortcuts import render
from rest_framework import viewsets
from .models import Vendedor
from .serializers import VendedoresSerializer

from vendas.models import Venda
from .serializers import ComissaoMensalSerializer
# Create your views here.


class VendedoresViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedoresSerializer


class ComissoesViewSet(viewsets.ModelViewSet):
    serializer_class = ComissaoMensalSerializer

    def get_queryset(self):
        return Venda.objects.filter(mes=int(self.kwargs['mes'])).order_by('-comissao')
