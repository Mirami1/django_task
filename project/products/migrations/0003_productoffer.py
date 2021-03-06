# Generated by Django 3.1 on 2020-10-14 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201014_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Торговое предложение')),
                ('guid', models.CharField(max_length=100, verbose_name='guid')),
                ('article', models.CharField(max_length=30, verbose_name='Артикул')),
                ('description', models.TextField(verbose_name='Описание')),
                ('smallsize', models.BooleanField(verbose_name='Маленький ли размер?')),
                ('length', models.PositiveIntegerField(verbose_name='Длина')),
                ('width', models.PositiveIntegerField(verbose_name='Ширина')),
                ('height', models.PositiveIntegerField(verbose_name='Высота')),
                ('weight', models.FloatField(verbose_name='Вес')),
                ('isshoes', models.BooleanField(verbose_name='Обувь?')),
                ('mainprice', models.FloatField(blank=True, default=0.0, verbose_name='Цена')),
                ('mainold_price', models.FloatField(blank=True, default=0.0, verbose_name='Старая цена')),
                ('is_new', models.BooleanField(verbose_name='Новинка?')),
                ('is_hit', models.BooleanField(verbose_name='Хит продаж?')),
                ('is_set', models.BooleanField(verbose_name='Набор?')),
                ('is_sale', models.BooleanField(verbose_name='Распродажа?')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='Количество')),
                ('addprods', models.ManyToManyField(related_name='_productoffer_addprods_+', to='products.ProductOffer', verbose_name='Похожие')),
                ('analogs', models.ManyToManyField(related_name='_productoffer_analogs_+', to='products.ProductOffer', verbose_name='Аналоги')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brands', verbose_name='Бренд')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.collection', verbose_name='Коллекция')),
                ('designs', models.ManyToManyField(to='products.Design', verbose_name='Дизайн')),
                ('gender_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.gendertype', verbose_name='Половая принадлежность')),
                ('images', models.ManyToManyField(related_name='images', to='products.Image', verbose_name='Фотографии')),
                ('is_mainphoto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.image', verbose_name='Фотография')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.manufacturer', verbose_name='Производитель')),
                ('prodtypes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.typemodel', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Предложение',
                'verbose_name_plural': 'Предложения',
            },
        ),
    ]
