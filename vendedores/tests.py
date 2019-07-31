from django.test import TestCase
from decimal import Decimal
from planos.models import PlanoComissoes
from vendedores.models import Vendedor


class VendedoresModelTest(TestCase):
    def test_deve_criar_vendedor(self):
        """
        Deve criar um vendedor
        """
        plano_comissao = PlanoComissoes(
            descricao="teste",
            valor_minimo=Decimal("0.0"),
            percent_min=Decimal("0.5"),
            percent_max=Decimal("1.0"),
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
        self.assertEqual(vendedor.id_vendedor, 1)

