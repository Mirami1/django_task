# Generated by Django 3.1 on 2020-10-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20201016_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristics',
            name='article',
            field=models.TextField(null=True, verbose_name='Артикул'),
        ),
    ]
