# Generated by Django 3.1 on 2020-10-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20201016_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imagemask',
            field=models.ImageField(blank=True, max_length=500, upload_to='images/%Y/%m/', verbose_name='Путь к картинке'),
        ),
    ]
