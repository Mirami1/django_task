# Generated by Django 3.1 on 2020-10-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20201016_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristics',
            name='article',
            field=models.CharField(max_length=500, verbose_name='Артикул'),
        ),
    ]