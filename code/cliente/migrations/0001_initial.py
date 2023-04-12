# Generated by Django 4.1.7 on 2023-04-11 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cpf_cnpj', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('PF', 'Pessoa Fisica'), ('PJ', 'Pessoa Juridica')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='ParteADV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cpf_cnpj', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('PF', 'Pessoa Fisica'), ('PJ', 'Pessoa Juridica')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Parte ADV',
            },
        ),
        migrations.CreateModel(
            name='ParteADVEndereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(default='Não Identificado', max_length=255)),
                ('complemento', models.CharField(default='Não Identificado', max_length=255)),
                ('cep', models.CharField(default='Não Identificado', max_length=30)),
                ('parte_adv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.parteadv')),
            ],
        ),
        migrations.CreateModel(
            name='ClienteEndereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(default='Não Identificado', max_length=255)),
                ('complemento', models.CharField(default='Não Identificado', max_length=255)),
                ('cep', models.CharField(default='Não Identificado', max_length=255)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
        ),
    ]