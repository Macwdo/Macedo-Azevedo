# Generated by Django 4.1.7 on 2023-04-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advogado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advogado',
            name='oab',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]