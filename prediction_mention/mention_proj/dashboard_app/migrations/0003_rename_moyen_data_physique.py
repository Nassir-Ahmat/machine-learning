# Generated by Django 4.0 on 2022-06-06 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0002_data_moyen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='moyen',
            new_name='physique',
        ),
    ]
