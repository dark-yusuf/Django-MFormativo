# Generated by Django 3.2.4 on 2021-08-16 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_auto_20210816_0622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='rut',
        ),
    ]
