# Generated by Django 4.1.7 on 2023-05-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_alter_clienteendereco_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
