from django.db import models
from django.core.validators import MinValueValidator
from planos.models import PlanoComissoes
from .validators import validate_CPF

# Create your models here.
class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True, verbose_name="Código vendedor")
    nome = models.CharField(max_length=100, null=False, verbose_name="Nome")
    cpf = models.CharField(
        max_length=14, null=False, validators=[validate_CPF], verbose_name="CPF"
    )
    endereco = models.TextField(null=False, verbose_name="Endereço")
    telefone = models.CharField(max_length=14, null=False, verbose_name="Telefone")
    idade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0)], null=False, verbose_name="Idade"
    )
    email = models.EmailField(null=False, verbose_name="E-mail")
    plano = models.ForeignKey(
        PlanoComissoes, on_delete=models.CASCADE, verbose_name="Plano de Comissão"
    )

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return self.nome

