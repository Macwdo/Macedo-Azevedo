# Generated by Django 4.1.4 on 2022-12-13 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0003_alter_arquivomodels_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivomodels',
            name='nome',
            field=models.CharField(default='Nada', max_length=20),
        ),
    ]
