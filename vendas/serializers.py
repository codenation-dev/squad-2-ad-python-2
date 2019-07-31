from rest_framework import serializers
from .models import Venda
from decimal import Decimal
from .validators import calcular_comissao


class VendasSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        vendas_mensais = validated_data["valor"]
        plano_do_vendedor = validated_data["id_vendedor"].plano
        validated_data["comissao"] = calcular_comissao(
            vendas_mensais, plano_do_vendedor
        )
        return Venda.objects.create(**validated_data)

    class Meta:
        model = Venda
        fields = ("id_venda", "id_vendedor", "mes", "valor")
