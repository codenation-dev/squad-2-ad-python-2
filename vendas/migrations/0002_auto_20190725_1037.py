# Generated by Django 2.2.3 on 2019-07-25 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0004_auto_20190715_1603'),
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='venda',
            unique_together={('id_vendedor', 'mes')},
        ),
    ]
