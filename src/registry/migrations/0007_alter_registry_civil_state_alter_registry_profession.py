# Generated by Django 4.1.7 on 2023-06-16 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0006_alter_registrycnpj_registry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='civil_state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registry',
            name='profession',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]