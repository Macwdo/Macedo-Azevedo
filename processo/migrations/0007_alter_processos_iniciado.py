# Generated by Django 4.1.4 on 2023-01-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0006_alter_processos_iniciado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processos',
            name='iniciado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
