# Generated by Django 4.1.7 on 2023-03-31 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_rename_registro_cliente_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parteadv',
            name='cpf_cnpj',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
