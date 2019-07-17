from rest_framework import serializers
from .models import Venda

# Serializers define the API representation.


class VendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ("id_venda", "id_vendedor", "mes", "valor")
