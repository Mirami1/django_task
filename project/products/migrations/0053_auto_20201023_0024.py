# Generated by Django 3.1 on 2020-10-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0052_auto_20201022_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typemodel',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название типа'),
        ),
        migrations.AlterField(
            model_name='typemodel',
            name='nametypeid',
            field=models.PositiveIntegerField(default=0, verbose_name='id типа'),
        ),
    ]
