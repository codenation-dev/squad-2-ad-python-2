from rest_framework import serializers
from .models import Vendedor
from vendas.models import Venda

# Serializers define the API representation.


class VendedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ("id_vendedor", "nome", "cpf", "endereco", "idade", "email", "plano")


class ComissaoMensalSerializer(serializers.ModelSerializer):
    comissao = serializers.SerializerMethodField()
    class Meta:
        model = Venda
        fields = ("id_vendedor", "mes", "comissao")


    def get_comissao(self, isinstance):
        return (isinstance.comissao.url if isinstance.comissao else 0.00)
