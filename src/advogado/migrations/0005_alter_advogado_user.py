# Generated by Django 4.1.7 on 2023-06-13 03:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advogado', '0004_alter_advogado_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advogado',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lawyer_user', to=settings.AUTH_USER_MODEL),
        ),
    ]