# Generated by Django 4.1.7 on 2023-03-09 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('advogado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_processo', models.CharField(max_length=25, unique=True)),
                ('posicao', models.CharField(choices=[('Autor', 'Autor'), ('Réu', 'Réu')], max_length=5)),
                ('assunto', models.CharField(choices=[('Trabalhista', 'Direito Trabalhista'), ('Previdenciário', 'Direito Previdenciário'), ('Civil', 'Direito Civil')], max_length=15)),
                ('observacoes', models.CharField(blank=True, default='Sem observações', max_length=255, null=True)),
                ('municipio', models.CharField(max_length=40)),
                ('estado', models.CharField(max_length=20)),
                ('n_vara', models.CharField(max_length=30)),
                ('vara', models.CharField(max_length=50)),
                ('iniciado', models.DateTimeField(auto_now_add=True)),
                ('finalizado', models.DateTimeField(blank=True, null=True)),
                ('advogado_responsavel', models.ForeignKey(default='Não Informado', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advogado_responsavel', to='advogado.advogado')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clientes', to='cliente.cliente')),
                ('cliente_de', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='advogado.advogado')),
                ('colaborador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='colaborador', to='advogado.advogado')),
                ('parte_adversa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.parteadv')),
            ],
            options={
                'verbose_name_plural': 'Processos',
            },
        ),
        migrations.CreateModel(
            name='ProcessosHonorarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referente', models.CharField(max_length=255)),
                ('valor', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processo.processos')),
                ('responsavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='advogado.advogado')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessosAnexos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processo.processos')),
            ],
        ),
    ]
