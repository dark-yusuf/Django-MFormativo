# Generated by Django 3.2.4 on 2021-08-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20210816_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
