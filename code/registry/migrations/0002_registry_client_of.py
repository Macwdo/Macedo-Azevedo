# Generated by Django 4.1.7 on 2023-06-03 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advogado', '0002_initial'),
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registry',
            name='client_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_of', to='advogado.advogado'),
        ),
    ]
