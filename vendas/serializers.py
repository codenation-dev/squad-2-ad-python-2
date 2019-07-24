from rest_framework import serializers
from .models import Venda
from decimal import Decimal


class VendasSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        vendas_mensais = validated_data["valor"]
        plano_do_vendedor = validated_data["id_vendedor"].plano
        comissao = Decimal(0.0)

        if vendas_mensais:
            if plano_do_vendedor.valor_minimo > vendas_mensais:
                comissao = (plano_do_vendedor.percent_max / 100) * vendas_mensais
            else:
                comissao = (plano_do_vendedor.percent_min / 100) * vendas_mensais

        validated_data["comissao"] = comissao
        return Venda.objects.create(**validated_data)

    class Meta:
        model = Venda
        fields = ("id_venda", "id_vendedor", "mes", "valor")
