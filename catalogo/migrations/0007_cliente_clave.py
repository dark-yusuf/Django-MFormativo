# Generated by Django 3.2.4 on 2021-08-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20210816_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='clave',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
