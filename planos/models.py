from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.core.exceptions import ValidationError
from .validators import validate_percent_max_menor_que_percent_min

# Create your models here.


class PlanoComissoes(models.Model):
    id_plano = models.AutoField(
        primary_key=True, verbose_name="Código do plano")
    descricao = models.CharField(
        max_length=100, null=False, verbose_name="Descrição")
    valor_minimo = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Valor mínimo",
        validators=[MinValueValidator(Decimal('0.0'))]
    )
    percent_min = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="% mínimo",
        validators=[MinValueValidator(Decimal('0.0'))]
    )
    percent_max = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="% máximo",
        validators=[MinValueValidator(Decimal('0.0'))]
    )

    def clean(self):
        validate_percent_max_menor_que_percent_min(self.percent_max, self.percent_min)

    class Meta:
        ordering = ["descricao"]
        verbose_name = "Plano de Comissão"
        verbose_name_plural = "Planos de Comissões"

    def __str__(self):
        return self.descricao
