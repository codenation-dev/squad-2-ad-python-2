from rest_framework import serializers
from .models import Vendedor

# Serializers define the API representation.


class VendedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ("id_vendedor", "nome", "cpf", "endereco", "idade", "email", "plano")
