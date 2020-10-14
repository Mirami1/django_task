from django.db import models


class Brands(models.Model):
    """
    Добавить уровни (Структура дерева ?)
    """
    name = models.CharField(verbose_name='Название бренда', max_length=256, unique=True)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)
    level = models.PositiveSmallIntegerField(verbose_name='Уровень вложенности', default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(verbose_name='Название коллекции', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.name


class Design(models.Model):
    name = models.CharField(verbose_name='Название дизайна', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Дизайн'
        verbose_name_plural = 'Дизайны'

    def __str__(self):
        return self.name


class GenderType(models.Model):
    name = models.CharField(verbose_name='Принадлежность', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Половая принадлежность'
        verbose_name_plural = 'Половая принадлежность'

    def __str__(self):
        return self.name


class HashTag(models.Model):
    name = models.CharField(verbose_name='Название производителя', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Хэш-Тег'
        verbose_name_plural = 'Хэш-Теги'

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(verbose_name='Название Производителя', max_length=200, unique=True)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class TypeModel(models.Model):
    name = models.CharField(verbose_name='Название типа', max_length=200, unique=True)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(verbose_name='Название размера', max_length=200, unique=True)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Image(models.Model):
    """
    Типы и подтипы картинок?
    """
    imagename = models.CharField(verbose_name='Название картинки', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)
    imagesize = models.PositiveIntegerField(verbose_name='Размер картинки')
    imageext = models.CharField(verbose_name='Расширение картинки', max_length=20)
    imagemask = models.ImageField(verbose_name='Путь к картинке', upload_to='images/%Y/%m/', blank=True)
    imagetype = models.PositiveSmallIntegerField(verbose_name='Тип картинки', default=0)
    imagesubtype = models.PositiveSmallIntegerField(verbose_name='Подтип картинки', null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.imagename
class NomenSet(models.Model):
    namesetprodtype = models.SmallIntegerField(verbose_name='Положение в наборе',unique=True)
    guid = models.CharField(verbose_name='guid', max_length=100)

    class Meta:
        verbose_name = 'Положение товара в наборе'
        verbose_name_plural = 'Положения товаров в наборе'

    def __str__(self):
        return self.name

class ProductOffer(models.Model):
    name = models.CharField(verbose_name='Торговое предложение', max_length=256)
    guid = models.CharField(verbose_name='guid', max_length=100)
    article = models.CharField(verbose_name='Артикул', max_length=30)
    description = models.TextField(verbose_name='Описание')
    smallsize = models.BooleanField(verbose_name='Маленький ли размер?')
    length = models.PositiveIntegerField(verbose_name='Длина')
    width = models.PositiveIntegerField(verbose_name='Ширина')
    height = models.PositiveIntegerField(verbose_name='Высота')
    weight = models.FloatField(verbose_name='Вес')
    isshoes = models.BooleanField(verbose_name='Обувь?')
    # artexh
    mainprice = models.FloatField(verbose_name='Цена', default=0.0, blank=True)
    mainold_price = models.FloatField(verbose_name='Старая цена', default=0.0, blank=True)
    is_new = models.BooleanField(verbose_name='Новинка?')
    is_hit = models.BooleanField(verbose_name='Хит продаж?')
    is_mainphoto = models.ForeignKey(Image, verbose_name='Фотография', on_delete=models.CASCADE)
    is_set = models.BooleanField(verbose_name='Набор?')
    is_sale = models.BooleanField(verbose_name='Распродажа?')
    # maintenance

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, verbose_name='Коллекция', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name='Бренд')
    gender_type = models.ForeignKey(GenderType, verbose_name='Половая принадлежность', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.CASCADE)

    prodtypes = models.ForeignKey(TypeModel, verbose_name='Тип', on_delete=models.CASCADE)
    designs = models.ManyToManyField(Design, verbose_name='Дизайн')
    images = models.ManyToManyField(Image, verbose_name='Фотографии', related_name='image_set')
    analogs = models.ManyToManyField("self", verbose_name='Аналоги')
    addprods = models.ManyToManyField("self", verbose_name='Похожие')
    count = models.PositiveSmallIntegerField(verbose_name='Количество', default=0)

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=200)
    guid = models.CharField(verbose_name='guid', max_length=100)
    # isshoestatamatr
    isshoes = models.BooleanField(verbose_name='Обувь?')
    articleh = models.CharField(verbose_name='Артикул', max_length=40)
    price = models.FloatField(verbose_name='Цена', default=0.0, blank=True)
    old_price = models.FloatField(verbose_name='Старая цена', default=0.0, blank=True)
    count = models.PositiveSmallIntegerField(verbose_name='Количество', default=0)
    product_offer = models.ForeignKey(ProductOffer, on_delete=models.SET_NULL, null=True, related_name='product',
                                      verbose_name='Торговое предложение')
    images = models.ManyToManyField(Image, verbose_name='Фотографии', related_name='images')
    size = models.ForeignKey(Size, verbose_name='Размер', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    class ProductOfferSet(models.Model):
        name = models.CharField(verbose_name='Торговое предложение', max_length=256)
        guid = models.CharField(verbose_name='guid', max_length=100)
        article = models.CharField(verbose_name='Артикул', max_length=30)
        description = models.TextField(verbose_name='Описание')
        smallsize = models.BooleanField(verbose_name='Маленький ли размер?')
        length = models.PositiveIntegerField(verbose_name='Длина')
        width = models.PositiveIntegerField(verbose_name='Ширина')
        height = models.PositiveIntegerField(verbose_name='Высота')
        weight = models.FloatField(verbose_name='Вес')
        isshoes = models.BooleanField(verbose_name='Обувь?')
        mainprice = models.FloatField(verbose_name='Цена', default=0.0, blank=True)
        subprodtype = models.PositiveSmallIntegerField(verbose_name='Подтип', default=0)

        category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
        collection = models.ForeignKey(Collection, verbose_name='Коллекция', on_delete=models.CASCADE)
        brand = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name='Бренд')
        manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.CASCADE)

        is_new = models.BooleanField(verbose_name='Новинка?')
        is_hit = models.BooleanField(verbose_name='Хит продаж?')
        is_mainphoto = models.ForeignKey(Image, verbose_name='Фотография', on_delete=models.CASCADE)
        is_set = models.BooleanField(verbose_name='Набор?')
        is_sale = models.BooleanField(verbose_name='Распродажа?')

        # maintenance
        gender_type = models.ForeignKey(GenderType, verbose_name='Половая принадлежность', on_delete=models.CASCADE)

        images = models.ManyToManyField(Image, verbose_name='Фотографии', related_name='images_in_productset')
        analogs = models.ManyToManyField("self", verbose_name='Аналоги')
        addprods = models.ManyToManyField("self", verbose_name='Похожие')

        nomen_sets= models.ManyToManyField(NomenSet,verbose_name='Положение товаров в наборе')

        class Meta:
            verbose_name = 'Набор'
            verbose_name_plural = 'Наборы'

        def __str__(self):
            return self.name
