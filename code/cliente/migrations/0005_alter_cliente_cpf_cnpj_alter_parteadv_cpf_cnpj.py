# Generated by Django 4.1.7 on 2023-04-07 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_alter_parteadv_cpf_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf_cnpj',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='parteadv',
            name='cpf_cnpj',
            field=models.CharField(max_length=30),
        ),
    ]
