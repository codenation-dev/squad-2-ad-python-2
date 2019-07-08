from rest_framework import serializers
from .models import PlanoComissoes
# Serializers define the API representation.


class PlanosSerializer(serializers.ModelSerializer):
    class Meta:
        model =PlanoComissoes
        fields = ('id_plano', 'descricao', 'valor_minimo', 'percent_min', 'percent_max')
