# Generated by Django 3.1 on 2020-10-19 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0047_auto_20201019_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.collection', verbose_name='Коллекция'),
        ),
        migrations.AlterField(
            model_name='set',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.manufacturer', verbose_name='Производитель'),
        ),
    ]
