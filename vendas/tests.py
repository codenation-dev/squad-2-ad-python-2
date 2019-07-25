from django.test import TestCase
from decimal import Decimal
from planos.models import PlanoComissoes
from vendedores.models import Vendedor
from vendas.models import Venda


class VendasModelTests(TestCase):
    def test_deve_calcular_comissao_mensal_valor_minimo(self):
        """
        Deve calcular a comissão em cima de uma venda mensal
        """
        plano_comissao = PlanoComissoes(
            descricao="teste",
            valor_minimo=Decimal("100.0"),
            percent_min=Decimal("1.0"),
            percent_max=Decimal("2.0"),
        )
        plano_comissao.save()
        vendedor = Vendedor(
            nome="Paulão",
            cpf="69252248005",
            endereco="Rua São Paulo",
            idade=18,
            email="paulao@gmail.com",
            plano=plano_comissao,
        )
        vendedor.save()
        venda = Venda(id_vendedor=vendedor, mes=1, valor=100)
        venda.save()

        self.assertEqual(venda.comissao, Decimal("1.0"))

