from rest_framework import serializers
from .models import PlanoComissoes
from .validators import validate_percent_max_menor_que_percent_min
# Serializers define the API representation.


class PlanosSerializer(serializers.ModelSerializer):

    def validate(self, data):
        percent_max = data['percent_max']
        percent_min = data['percent_min']
        validate_percent_max_menor_que_percent_min(percent_max, percent_min)

    class Meta:
        model = PlanoComissoes
        fields = ('id_plano', 'descricao', 'valor_minimo',
                  'percent_min', 'percent_max')
