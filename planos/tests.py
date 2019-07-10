from planos.models import PlanoComissoes
from decimal import Decimal
from django.test import TestCase
from django.core.exceptions import ValidationError


class PlanoModelTests(TestCase):

    def test_deve_criar_plano_comissao(self):
        """
        Deve criar um plano de comissão
        """
        planoComissao = PlanoComissoes(descricao='teste', valor_minimo=Decimal('0.0'), percent_min=Decimal(
            '0.5'), percent_max=Decimal('1.0'))
        planoComissao.save()
        self.assertEqual(planoComissao.id_plano, 1)

    def test_nao_deve_criar_plano_com_valores_negativos(self):
        """
        Deve discriminar um erro para cada um dos campos com valores negativos no plano de comissão
        """
        planoComissao = PlanoComissoes(descricao='teste', valor_minimo=Decimal('-1.0'), percent_min=Decimal(
            '-0.5'), percent_max=Decimal('-1.0'))

        try:
            planoComissao.clean_fields()
            self.fail('Deveria ter validado valores negativos')
        except ValidationError as valueErrors:
            validation_errors = valueErrors.error_dict
            self.assertIsNotNone(validation_errors['valor_minimo'])
            self.assertIsNotNone(validation_errors['percent_min'])
            self.assertIsNotNone(validation_errors['percent_max'])
