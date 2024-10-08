# Generated by Django 4.1.7 on 2023-06-12 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advogado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('civil_state', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('client_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registry_client_of', to='advogado.advogado')),
            ],
            options={
                'verbose_name_plural': 'Registro',
            },
        ),
        migrations.CreateModel(
            name='RegistryCnpj',
            fields=[
                ('registry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='registry_cnpj', serialize=False, to='registry.registry')),
                ('cnpj', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='RegistryCpf',
            fields=[
                ('registry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='registry_cpf', serialize=False, to='registry.registry')),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='RegistryContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('registry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registry_contact', to='registry.registry')),
            ],
            options={
                'verbose_name_plural': 'Contato do registro',
            },
        ),
        migrations.CreateModel(
            name='RegistryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('address_number', models.CharField(max_length=50)),
                ('complement', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
                ('reference', models.CharField(max_length=255)),
                ('registry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registry_address', to='registry.registry')),
            ],
            options={
                'verbose_name_plural': 'Endereço dos registros',
            },
        ),
    ]
