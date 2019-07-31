from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Venda
from .serializers import VendasSerializer
from rest_framework.response import Response


class VendasViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendasSerializer


@api_view(["POST"])
def notificar_vendedores(request):
    """
    Dado o ID de um vendedor o seu último valor de vendas, recupera as vendas dos últimos cinco meses.
    É então realizado o cálculo da média ponderada levando em consideração as maiores comissões como com o maior peso.
    Por fim, é realizado um buffer na média de 10% do seu valor, caso este seja menor que o valor base, é retornado que o vendedor deve ser notificado.
    """

    vendedor = request.query_params["vendedor"]
    valor = request.query_params["valor"]

    vendas = Venda.objects.filter(
        id_vendedor=vendedor).order_by("-mes", "-comissao")[:5]
    total = 0
    for cont, venda in enumerate(vendas):
        total = total + (len(vendas) - cont) * venda.comissao
    media = float(total / len(vendas)) * 0.9

    if media < float(valor):
        return Response({"notificar": True})
    else:
        return Response({"notificar": False})
