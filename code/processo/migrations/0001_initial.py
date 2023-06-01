# Generated by Django 4.1.7 on 2023-06-01 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advogado', '0001_initial'),
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_processo', models.CharField(max_length=25)),
                ('posicao', models.CharField(choices=[('autor', 'Autor'), ('reu', 'Réu')], max_length=5)),
                ('assunto', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('vara', models.CharField(max_length=50)),
                ('observacoes', models.TextField()),
                ('iniciado', models.DateTimeField()),
                ('finalizado', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('advogado_responsavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lawyer', to='advogado.advogado')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client', to='registry.registry')),
                ('cliente_de', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_of', to='advogado.advogado')),
                ('colaborador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='colaborator_lawyer', to='advogado.advogado')),
                ('indicado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='indicated_by', to='registry.registry')),
                ('parte_adversa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adverse_part', to='registry.registry')),
            ],
            options={
                'verbose_name_plural': 'Processos',
            },
        ),
        migrations.CreateModel(
            name='ProcessosAssuntos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessosMovimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_movimento', models.CharField(default='Vazio', max_length=255)),
                ('last_date', models.CharField(max_length=10)),
                ('data', models.TextField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processo.processos')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessosHonorarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referente', models.CharField(max_length=255)),
                ('valor', models.FloatField()),
                ('ganho', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('advogado_responsavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='advogado.advogado')),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processo_honorarios', to='processo.processos')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessosAnexos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_anexo', models.CharField(max_length=100)),
                ('arquivo', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processo_anexos', to='processo.processos')),
            ],
        ),
    ]
