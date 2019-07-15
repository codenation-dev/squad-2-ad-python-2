# Generated by Django 2.2.3 on 2019-07-15 19:03

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendedores', '0004_auto_20190715_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id_venda', models.AutoField(primary_key=True, serialize=False, verbose_name='Código venda')),
                ('mes', models.PositiveSmallIntegerField(choices=[(1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'), (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'), (9, 'Setembro'), (10, 'Otubro'), (11, 'Novembro'), (12, 'Dezembro')], verbose_name='Mês')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))], verbose_name='Valor da venda')),
                ('comissao', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=9, null=True, verbose_name='Valor da comissão')),
                ('id_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedores.Vendedor', verbose_name='Vendedor')),
            ],
            options={
                'verbose_name_plural': 'Vendas',
                'ordering': ['mes', 'id_vendedor'],
            },
        ),
    ]
