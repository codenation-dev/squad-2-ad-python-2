from rest_framework import serializers
from .models import Vendedor
from vendas.models import Venda


class VendedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ("id_vendedor", "nome", "cpf", "endereco", "idade", "email", "plano")


class ComissaoMensalSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='id_vendedor.nome')
    comissao = serializers.SerializerMethodField()
    class Meta:
        model = Venda
        fields = ("nome", "id_vendedor", "comissao")

    def get_comissao(self, isinstance):
        return (isinstance.comissao if isinstance.comissao else 0.00)
