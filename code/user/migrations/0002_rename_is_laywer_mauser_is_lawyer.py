# Generated by Django 4.1.7 on 2023-06-06 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mauser',
            old_name='is_laywer',
            new_name='is_lawyer',
        ),
    ]
