# Generated by Django 4.1.7 on 2023-06-12 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrycnpj',
            name='registry',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='cnpj', serialize=False, to='registry.registry'),
        ),
        migrations.AlterField(
            model_name='registrycpf',
            name='registry',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='cpf', serialize=False, to='registry.registry'),
        ),
    ]
