# Generated by Django 4.1.4 on 2022-12-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custos',
            options={'verbose_name_plural': 'Custos'},
        ),
        migrations.AlterField(
            model_name='custos',
            name='pago',
            field=models.BooleanField(default=False),
        ),
    ]
