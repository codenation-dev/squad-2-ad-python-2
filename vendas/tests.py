from django.test import TestCase
from decimal import Decimal
from planos.models import PlanoComissoes
from vendedores.models import Vendedor
from vendas.models import Venda


class VendasModelTests(TestCase):
    def test_deve_calcular_comissao_mensal_valor_maximo(self):
        """
        Deve calcular a comissão com percentual maximo ao salvar uma venda mensal.
        """
        venda = self.create_venda_com_valor(50)
        self.assertEqual(venda.comissao, Decimal("0.5"))

    def test_deve_calcular_comissao_mensal_valor_minimo(self):
        """
        Deve calcular a comissão com percentual minimo ao salvar uma venda mensal.
        """
        venda = self.create_venda_com_valor(100)
        self.assertEqual(venda.comissao, Decimal("2.0"))

    def create_venda_com_valor(self, valor_venda):
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
        venda = Venda(id_vendedor=vendedor, mes=1, valor=valor_venda)
        venda.save()
        return venda
