# Generated by Django 2.2.3 on 2019-07-15 18:23

from django.db import migrations, models
import vendedores.validators


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0002_auto_20190715_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='cpf',
            field=models.CharField(max_length=14, validators=[vendedores.validators.validate_CPF], verbose_name='CPF'),
        ),
    ]
