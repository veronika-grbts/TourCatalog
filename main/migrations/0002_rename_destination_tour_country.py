# Generated by Django 4.2.16 on 2024-12-06 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='destination',
            new_name='country',
        ),
    ]