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
<<<<<<< HEAD
def notificar_vededores(request):
=======
def check_comission(request):
>>>>>>> 8ff6c50743b7ce73891b923352bc385a2956b1ca

    vendedor = request.query_params["vendedor"]
    valor = request.query_params["valor"]

    vendas = Venda.objects.filter(id_vendedor=vendedor).order_by("-comissao")[:5]
    total = 0
    for cont, venda in enumerate(vendas):
        total = total + (len(vendas) - cont) * venda.comissao
    media = float(total / len(vendas)) * 0.9

    if media < float(valor):
<<<<<<< HEAD
        return Response({"notificar": True})
    else:
        return Response({"notificar": False})
=======
        return Response({"notificar": False})
    else:
        return Response({"notificar": True})
>>>>>>> 8ff6c50743b7ce73891b923352bc385a2956b1ca

