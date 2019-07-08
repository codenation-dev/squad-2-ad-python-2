from django.db import models

# Create your models here.
class PlanoComissoes(models.Model):
    id_plano = models.AutoField(primary_key=True, verbose_name="Código do plano")
    descricao = models.CharField(max_length=100, null=False, verbose_name="Descrição")
    valor_minimo = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Valor mínimo"
    )
    percent_min = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="% mínimo"
    )
    percent_max = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="% máximo"
    )

    class Meta:
        ordering = ["descricao"]
        verbose_name = "Plano de Comissão"
        verbose_name_plural = "Planos de Comissões"

    def __str__(self):
        return self.descricao
