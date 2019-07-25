from django.shortcuts import render
from rest_framework import viewsets
from .models import Venda
from .serializers import VendasSerializer
from rest_framework.response import Response


class VendasViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendasSerializer


def check_comission(request):

    data = request.data
    vendedor = data["vendedor"]
    valor = data["valor"]

    vendas = Venda.objects.filter(id_vendedor=vendedor).order_by("valor")[:5]
    total = 0
    for cont, venda in enumerate(vendas):
        total = total + cont * venda.valor
    media = float((total / len(vendas))) * 0.9

    if media < float(valor):
        return Response({"notificar": False})
    else:
        return Response({"notificar": True})

