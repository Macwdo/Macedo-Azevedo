# Generated by Django 4.1.4 on 2023-02-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_alter_cliente_registro_alter_parteadv_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='registro',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='parteadv',
            name='registro',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
