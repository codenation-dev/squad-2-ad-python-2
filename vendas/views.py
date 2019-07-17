from django.shortcuts import render
from rest_framework import viewsets
from .models import Venda
from .serializers import VendasSerializer
# Create your views here.


class VendasViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendasSerializer
