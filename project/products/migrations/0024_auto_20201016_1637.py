# Generated by Django 3.1 on 2020-10-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20201016_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristics',
            name='maintenance',
            field=models.CharField(max_length=2000, verbose_name='Уход за товаром'),
        ),
    ]