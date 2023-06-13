# Generated by Django 4.1.7 on 2023-06-13 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0005_alter_registrycnpj_registry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrycnpj',
            name='registry',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='registry_cnpj', serialize=False, to='registry.registry'),
        ),
        migrations.AlterField(
            model_name='registrycpf',
            name='registry',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='registry_cpf', serialize=False, to='registry.registry'),
        ),
    ]
