from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from vendedores.models import Vendedor
from .validators import calcular_comissao


class Venda(models.Model):
    MESES = (
        (1, "Janeiro"),
        (2, "Fevereiro"),
        (3, "Março"),
        (4, "Abril"),
        (5, "Maio"),
        (6, "Junho"),
        (7, "Julho"),
        (8, "Agosto"),
        (9, "Setembro"),
        (10, "Outubro"),
        (11, "Novembro"),
        (12, "Dezembro"),
    )

    id_venda = models.AutoField(primary_key=True, verbose_name="Código venda")
    id_vendedor = models.ForeignKey(
        Vendedor, on_delete=models.CASCADE, verbose_name="Vendedor"
    )
    mes = models.PositiveSmallIntegerField(choices=MESES, verbose_name="Mês")
    valor = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.0"))],
        verbose_name="Valor da venda",
    )
    comissao = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        editable=False,
        null=True,
        blank=True,
        verbose_name="Valor da comissão",
    )

    class Meta:
        ordering = ["mes", "id_vendedor"]
        verbose_name_plural = "Vendas"
        unique_together = ("id_vendedor", "mes")

    def __str__(self):
        return f"{self.mes} - {self.id_vendedor}"

    def save(self, *args, **kwargs):
        self.comissao = calcular_comissao(self.valor, self.id_vendedor.plano)
        super(Venda, self).save(*args, **kwargs)
