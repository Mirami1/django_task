from django.db import models


class Brands(models.Model):
    name = models.CharField(verbose_name='Название бренда', max_length=256)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.guid


class Region(models.Model):
    name = models.CharField(verbose_name='Регион', max_length=100)
    code = models.IntegerField(verbose_name='Код региона',null=True)

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(verbose_name='Город', max_length=100)
    code = models.IntegerField(verbose_name='Код города')
    region = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Добавить уровни (Структура дерева ?)
    """
    name = models.CharField(verbose_name='Название категории', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)
    level = models.PositiveSmallIntegerField(verbose_name='Уровень вложенности', default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.guid


class Collection(models.Model):
    name = models.CharField(verbose_name='Название коллекции', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.guid


class Design(models.Model):
    name = models.CharField(verbose_name='Название дизайна', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Дизайн'
        verbose_name_plural = 'Дизайны'

    def __str__(self):
        return self.guid


class GenderType(models.Model):
    name = models.CharField(verbose_name='Принадлежность', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Половая принадлежность'
        verbose_name_plural = 'Половая принадлежность'

    def __str__(self):
        return self.guid


class HashTag(models.Model):
    name = models.CharField(verbose_name='Название производителя', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Хэш-Тег'
        verbose_name_plural = 'Хэш-Теги'

    def __str__(self):
        return self.guid


class Manufacturer(models.Model):
    name = models.CharField(verbose_name='Название Производителя', max_length=200, unique=True)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.guid


class TypeModel(models.Model):
    name = models.CharField(verbose_name='Название типа', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)
    nametypeid = models.PositiveIntegerField(verbose_name='id типа', default=0)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.guid


class Size(models.Model):
    name = models.CharField(verbose_name='Название размера', max_length=200, unique=True)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.guid


class Image(models.Model):
    """
    Типы и подтипы картинок?
    """
    imagename = models.TextField(verbose_name='Название картинки')
    guid = models.TextField(verbose_name='guid')
    imagesize = models.PositiveIntegerField(verbose_name='Размер картинки')
    imageext = models.TextField(verbose_name='Расширение картинки')
    imagemask = models.ImageField(verbose_name='Путь к картинке', upload_to='images/%Y/%m/', blank=True, max_length=500)
    imagetype = models.PositiveSmallIntegerField(verbose_name='Тип картинки', default=0)
    imagesubtype = models.PositiveSmallIntegerField(verbose_name='Подтип картинки', null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.imagemask.__str__()


class NomenSet(models.Model):
    nomensetpodtype = models.SmallIntegerField(verbose_name='Положение в наборе')
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Положение товара в наборе'
        verbose_name_plural = 'Положения товаров в наборе'

    def __str__(self):
        return self.guid


class Color(models.Model):
    nameid = models.PositiveIntegerField(verbose_name='id имени', unique=True)
    name = models.CharField(verbose_name='Название цвета', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)
    nametwo = models.CharField(verbose_name='Дополнительное название', max_length=200, null=True)
    hexcode = models.CharField(verbose_name='Цвет в числовом представлении', max_length=100, null=True)
    images = models.ManyToManyField(Image, verbose_name='Фотографии', related_name='color_images')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.guid


class Characteristics(models.Model):
    name = models.CharField(verbose_name='Характеристики товара', max_length=256)
    guid = models.CharField(verbose_name='guid', max_length=200)
    article = models.TextField(verbose_name='Артикул', null=True)
    description = models.TextField(verbose_name='Описание', null=True)
    composition = models.TextField(verbose_name='Сравнение', null=True)
    smallsize = models.BooleanField(verbose_name='Маленький ли размер?')
    length = models.PositiveIntegerField(verbose_name='Длина')
    width = models.PositiveIntegerField(verbose_name='Ширина')
    height = models.PositiveIntegerField(verbose_name='Высота')
    weight = models.FloatField(verbose_name='Вес')
    isshoes = models.BooleanField(verbose_name='Обувь?')
    artexh = models.CharField(verbose_name='Доп инфа + id цвета', max_length=256)
    mainprice = models.FloatField(verbose_name='Цена', default=0.0, blank=True)
    mainold_price = models.FloatField(verbose_name='Старая цена', default=0.0, blank=True)
    is_new = models.BooleanField(verbose_name='Новинка?')
    is_hit = models.BooleanField(verbose_name='Хит продаж?')
    is_mainphoto = models.ForeignKey(Image, verbose_name='Фотография', on_delete=models.CASCADE, null=True)
    is_set = models.BooleanField(verbose_name='Набор?')
    is_sale = models.BooleanField(verbose_name='Распродажа?')
    maintenance = models.TextField(verbose_name='Уход за товаром', null=True)

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, null=True)
    collection = models.ForeignKey(Collection, verbose_name='Коллекция', on_delete=models.CASCADE, null=True)
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name='Бренд', null=True)
    gendertype = models.ForeignKey(GenderType, verbose_name='Половая принадлежность', on_delete=models.CASCADE,
                                   null=True)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.CASCADE, null=True)

    prodtypes = models.ManyToManyField(TypeModel, verbose_name='Тип')
    designs = models.ManyToManyField(Design, verbose_name='Дизайн')
    images = models.ManyToManyField(Image, verbose_name='Фотографии', related_name='image_set')
    analogs = models.ManyToManyField("self", verbose_name='Аналоги')
    addprods = models.ManyToManyField("self", verbose_name='Похожие')
    count = models.PositiveSmallIntegerField(verbose_name='Количество', default=0)

    class Meta:
        verbose_name = 'Характеристики'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.guid


class Set(models.Model):
    name = models.CharField(verbose_name='Торговое предложение', max_length=256)
    guid = models.CharField(verbose_name='guid', max_length=100)
    article = models.CharField(verbose_name='Артикул', max_length=30)
    description = models.TextField(verbose_name='Описание', null=True)
    composition = models.TextField(verbose_name='Сравнение', null=True)
    smallsize = models.BooleanField(verbose_name='Маленький ли размер?')
    maintenance = models.TextField(verbose_name='Уход за товаром', null=True)
    length = models.PositiveIntegerField(verbose_name='Длина')
    width = models.PositiveIntegerField(verbose_name='Ширина')
    height = models.PositiveIntegerField(verbose_name='Высота')
    weight = models.FloatField(verbose_name='Вес')
    isshoes = models.BooleanField(verbose_name='Обувь?', null=True)
    mainprice = models.FloatField(verbose_name='Цена', default=0.0, blank=True)
    subprodtype = models.PositiveSmallIntegerField(verbose_name='Подтип', default=0)

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, null=True)
    collection = models.ForeignKey(Collection, verbose_name='Коллекция', on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name='Бренд', null=True)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.CASCADE, null=True)

    is_new = models.BooleanField(verbose_name='Новинка?')
    is_hit = models.BooleanField(verbose_name='Хит продаж?')
    is_mainphoto = models.ForeignKey(Image, verbose_name='Фотография', on_delete=models.CASCADE, null=True)
    is_set = models.BooleanField(verbose_name='Набор?')
    is_sale = models.BooleanField(verbose_name='Распродажа?')

    # maintenance
    gendertype = models.ForeignKey(GenderType, verbose_name='Половая принадлежность', on_delete=models.CASCADE,
                                   null=True)

    images = models.ManyToManyField(Image, verbose_name='Фотографии', related_name='images_in_productset')
    analogs = models.ManyToManyField("self", verbose_name='Аналоги')
    addprods = models.ManyToManyField("self", verbose_name='Похожие')

    nomen_sets = models.ManyToManyField(NomenSet, verbose_name='Положение товаров в наборе')

    class Meta:
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'

    def __str__(self):
        return self.guid


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)
    isshoes = models.BooleanField(verbose_name='Обувь?')
    articleh = models.CharField(verbose_name='Артикул', max_length=40, null=True)
    price = models.FloatField(verbose_name='Цена', default=0.0, blank=True)
    old_price = models.FloatField(verbose_name='Старая цена', default=0.0, blank=True)
    count = models.PositiveSmallIntegerField(verbose_name='Количество', default=0)
    characteristics = models.ForeignKey(Characteristics, on_delete=models.CASCADE, null=True, related_name='product',
                                        verbose_name='Характеристики товара')
    images = models.ManyToManyField(Image, verbose_name='Фотографии', related_name='images')
    size = models.ForeignKey(Size, verbose_name='Размер', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.guid
