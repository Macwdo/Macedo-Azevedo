# Generated by Django 4.1.7 on 2023-05-30 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processos',
            name='assunto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='processos',
            name='estado',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='processos',
            name='iniciado',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='processos',
            name='municipio',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='processos',
            name='observacoes',
            field=models.TextField(),
        ),
    ]
