# Generated by Django 4.1.4 on 2023-01-19 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_registro_alter_parteadv_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='registro',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='parteadv',
            name='registro',
            field=models.DateTimeField(),
        ),
    ]