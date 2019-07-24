from django.test import TestCase
from planos.models import PlanoComissoes
from vendedores.models import Vendedor
from vendas.models import Venda

# Create your tests here.
class VendasModelTests(TestCase):

    def test_deve_calcular_comissao_mensal(self):
        """
        Deve calcular a comissão em cima de uma venda mensal
        """
        Venda(id_vendedor=1)