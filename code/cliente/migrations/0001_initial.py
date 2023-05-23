# Generated by Django 4.1.7 on 2023-05-23 16:45

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
                ('cpf_cnpj', models.CharField(max_length=30)),
                ('estado_civil', models.CharField(max_length=100)),
                ('profissao', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('PF', 'Pessoa Fisica'), ('PJ', 'Pessoa Juridica')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='ClienteEndereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=50)),
                ('complemento', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_address', to='cliente.cliente')),
            ],
            options={
                'verbose_name_plural': 'Endereços do cliente',
            },
        ),
        migrations.CreateModel(
            name='ClienteContato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, null=True)),
                ('numero', models.CharField(max_length=20, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_contact', to='cliente.cliente')),
            ],
            options={
                'verbose_name_plural': 'Contatos do cliente',
            },
        ),
    ]
