from .models import *
import json


# Полная очитска всех таблиц в БД
def clear():
    Characteristics.objects.all().delete()
    Product.objects.all().delete()
    Set.objects.all().delete()
    Brands.objects.all().delete()
    Category.objects.all().delete()
    Collection.objects.all().delete()
    Color.objects.all().delete()
    Design.objects.all().delete()
    GenderType.objects.all().delete()
    HashTag.objects.all().delete()
    Manufacturer.objects.all().delete()
    TypeModel.objects.all().delete()
    Size.objects.all().delete()
    Image.objects.all().delete()
    NomenSet.objects.all().delete()
    Image.objects.all().delete()


# Загрузка вспомогательных таблиц
def load_sub_tables():
    print('ЗАГРУЗКА ДОПТАБЛИЦ')
    with open('get_directories.json', 'r', encoding='UTF-8') as json_file:

        data = json.load(json_file)
        for model in data['models']:

            if model['model'] == 'Collection':
                for item in model['items']:
                    Collection.objects.create(name=item['name'], guid=item['guid'])

            if model['model'] == 'Brands':
                for item in model['items']:
                    Brands.objects.create(name=item['name'], guid=item['guid'])

            if model['model'] == 'Manufacturer':
                for item in model['items']:
                    Manufacturer.objects.create(name=item['name'], guid=item['guid'])

            if model['model'] == 'Color':
                for item in model['items']:
                    images = []
                    if item['images'] != '':
                        images = get_images(im_item=item)

                    Color.objects.create(name=item['name'], guid=item['guid'], nameid=item['nameid'],
                                         nametwo=item.get('nametwo', None),
                                         hexcode=item.get('hexcode', None)).images.set(images)

            if model['model'] == 'Design':
                for item in model['items']:
                    Design.objects.create(name=item['name'], guid=item['guid'])

            if model['model'] == 'TypeModel':
                for item in model['items']:
                    TypeModel.objects.create(name=item['name'], guid=item['guid'], nametypeid=item['nametypeid'])

            if model['model'] == 'Size':
                for item in model['items']:
                    Size.objects.create(name=item['name'], guid=item['guid'])

            if model['model'] == 'hashtag':
                for item in model['items']:
                    HashTag.objects.create(name=item['name'], guid=item['guid'])

            if model['model'] == 'gendertype':
                for item in model['items']:
                    GenderType.objects.create(name=item['name'], guid=item['guid'])


# Загрузка таблицы с характеристиками товаров
def load_characteristics():
    print('ЗАГРУЗКА ХАРАКТЕРИСТИК')
    with open('get_products.json', 'r', encoding='UTF-8') as json_file:

        data = json.load(json_file)
        for model in data['models']:
            if model['model'] == 'ProductOffer':
                for item in model['items']:
                    # Загрузка полей, некоторые простые поля в обектах пусты!

                    guid = item['guid']
                    name = item['name']
                    article = item.get('article', None)
                    description = item.get('description', None)
                    composition = item.get('composition', None)
                    smallsize = item['smallsize']
                    length = item['length']
                    width = item['width']
                    height = item['height']
                    weight = item['weight']
                    isshoes = item['isshoes']
                    artexh = item['artexh']
                    mainprice = item['mainprice']
                    mainold_price = item['mainold_price']
                    is_new = item['is_new']
                    is_hit = item['is_hit']

                    # Очень часто это поле оказывается пустым или ссылающимся на отсутвующую фотографию
                    try:
                        is_mainphoto = Image.objects.get(guid=item.get('is_mainphoto', None))
                    except Image.DoesNotExist:
                        print('Без основной фотки guid=', item.get('is_mainphoto', None))
                        is_mainphoto = None

                    is_set = item['is_set']
                    is_sale = item['is_sale']
                    maintenance = item.get('maintenance', None)
                    count = item['count']

                    # В других внешних полях тоже!
                    try:
                        collection = Collection.objects.get(guid=item.get('collection', None))
                    except Collection.DoesNotExist:
                        print('Без коллекции guid=', item.get('collection', None))
                        collection = None

                    try:
                        brand = Brands.objects.get(guid=item.get('brand', None))
                    except Brands.DoesNotExist:
                        print('Без бренда guid=', item.get('brand', None))
                        brand = None

                    try:
                        manufacturer = Manufacturer.objects.get(guid=item.get('manufacturer', None))
                    except Manufacturer.DoesNotExist:
                        print('Без производителя guid=', item.get('manufacturer', None))
                        manufacturer = None

                    try:
                        gender_type = GenderType.objects.get(guid=item.get('gendertype', None))
                    except GenderType.DoesNotExist:
                        print('Без половой принадлежности guid=', item.get('gendertype', None))
                        gender_type = None

                    # Добавление полей, которые могут ссылаться на несколько обьектов
                    prod_types = []
                    designs = []
                    analogs = []
                    addprods = []
                    images = []

                    if item['prodtypes']:
                        for im in item['prodtypes']:
                            if TypeModel.objects.filter(guid=im['guid']).exists():
                                prod_types.append(TypeModel.objects.get(guid=im['guid']).id)
                            else:
                                print('TypeModel попался! guid=', im['guid'])

                    if item['desings']:
                        for im in item['desings']:
                            if Design.objects.filter(guid=im['guid']).exists():
                                designs.append(Design.objects.get(guid=im['guid']).id)
                            else:
                                print('Design попался! guid=', im['guid'])

                    if item['images'] != '':
                        images = get_images(im_item=item)

                    if item['analogs'] != '':
                        for im in item['analogs']:
                            if Characteristics.objects.filter(guid=im['guid']).exists():
                                analogs.append(Characteristics.objects.get(guid=im['guid']).id)
                            else:
                                print('Characteristics_1 попался, точнее не нашелся! guid=', im['guid'])

                    if item['addprods'] != '':
                        for im in item['addprods']:
                            if Characteristics.objects.filter(guid=im['guid']).exists():
                                addprods.append(Characteristics.objects.get(guid=im['guid']).id)
                            else:
                                print('Characteristics_2 попался, точнее не нашелся! guid=', im['guid'])

                    characteristics = Characteristics.objects.create(guid=guid, name=name, article=article,
                                                                     description=description,
                                                                     composition=composition, smallsize=smallsize,
                                                                     length=length,
                                                                     width=width,
                                                                     height=height, weight=weight, isshoes=isshoes,
                                                                     artexh=artexh,
                                                                     mainprice=mainprice,
                                                                     mainold_price=mainold_price, is_new=is_new,
                                                                     is_hit=is_hit,
                                                                     is_mainphoto=is_mainphoto,
                                                                     is_set=is_set, is_sale=is_sale,
                                                                     maintenance=maintenance,
                                                                     collection=collection, brand=brand,
                                                                     manufacturer=manufacturer,
                                                                     gender_type=gender_type, count=count,
                                                                     category=None)
                    # Добавление ключей к полям типа многие-ко-многим
                    if prod_types:
                        characteristics.prodtypes.add(*prod_types)
                    if designs:
                        characteristics.designs.add(*designs)
                    if analogs:
                        characteristics.analogs.add(*analogs)
                    if addprods:
                        characteristics.addprods.add(*addprods)
                    if images:
                        try:
                            characteristics.images.add(*images)
                        except Exception as e:
                            print(e.__str__())
                break


# Загрузка таблицы с товарами
def load_products():
    print('ЗАГРУЗКА ТОВАРОВ')
    with open('get_products.json', 'r', encoding='UTF-8') as json_file:

        data = json.load(json_file)
        for model in data['models']:
            if model['model'] == 'Product':
                for item in model['items']:
                    # Заполнение полей

                    guid = item['guid']
                    name = item['name']
                    isshoes = item['isshoes']

                    # Такая же проблема со связанными обьектами, либо несуществующий обьект, либо вообще нет
                    # такого поля в обьекте

                    try:
                        size = Size.objects.get(guid=item['size'])
                    except Size.DoesNotExist:
                        print('Не нашел размер guid=', item['size'])
                        size = None
                    except KeyError:
                        print('Не нашел размер в файле')
                        size = None
                    try:
                        characteristics = Characteristics.objects.get(guid=item['product_offer'])
                    except Characteristics.DoesNotExist:
                        print('Не нашел характеристики guid=', item['product_offer'])
                        characteristics = None
                    except KeyError:
                        print('Не нашел характеристику в файле')

                    articleh = item.get('articleh', None)
                    price = item['price']
                    old_price = item['old_price']
                    count = item['count']

                    images = []
                    if item['images'] != '':
                        images = get_images(im_item=item)

                    product = Product.objects.create(characteristics=characteristics, name=name, guid=guid,
                                                     isshoes=isshoes, size=size, articleh=articleh, count=count,
                                                     price=price, old_price=old_price)
                    if images:
                        product.images.add(*images)


# Загрузка наборов
def load_sets():
    print('ЗАГРУЗКА НАБОРОВ')
    with open('get_products.json', 'r', encoding='UTF-8') as json_file:

        data = json.load(json_file)
        for model in data['models']:
            if model['model'] == 'ProductOfferSet':
                for item in model['items']:
                    # Заполнение полей

                    guid = item['guid']
                    name = item['name']
                    article = item.get('article', None)
                    description = item.get('description', None)
                    composition = item.get('composition', None)
                    smallsize = item['smallsize']
                    length = item['length']
                    width = item['width']
                    height = item['height']
                    weight = item['weight']
                    mainprice = item['mainprice']
                    subprodtype = item.get('subprodtype', None)

                    # Такая же проблема со связанными обьектами, либо несуществующий обьект, либо вообще нет
                    # такого поля в обьекте

                    try:
                        collection = Collection.objects.get(guid=item.get('collection', None))
                    except Collection.DoesNotExist:
                        print('Без коллекции guid=', item.get('collection', None))
                        collection = None

                    try:
                        brand = Brands.objects.get(guid=item.get('brand', None))
                    except Brands.DoesNotExist:
                        print('Без бренда guid=', item.get('brand', None))
                        brand = None

                    try:
                        manufacturer = Manufacturer.objects.get(guid=item.get('manufacturer', None))
                    except Manufacturer.DoesNotExist:
                        print('Без производителя guid=', item.get('manufacturer', None))
                        manufacturer = None

                    try:
                        gender_type = GenderType.objects.get(guid=item.get('gendertype', None))
                    except GenderType.DoesNotExist:
                        print('Без половой принадлежности guid=', item.get('gendertype', None))
                        gender_type = None

                    is_new = item['is_new']
                    is_hit = item['is_hit']

                    try:
                        is_mainphoto = Image.objects.get(guid=item.get('is_mainphoto', None))
                    except Image.DoesNotExist:
                        print('Без основной фотки guid=', item.get('is_mainphoto', None))
                        is_mainphoto = None

                    is_set = item['is_set']
                    is_sale = item['is_sale']
                    maintenance = item.get('maintenance', None)

                    images = []
                    if item['images'] != '':
                        images = get_images(im_item=item)

                    nomen_sets = []

                    if item['nomen_sets'] != '':
                        for im in item['nomen_sets']:
                            if not NomenSet.objects.filter(guid=im['guid']).exists():
                                nomen_set = NomenSet.objects.create(guid=im['guid'],
                                                                    nomensetpodtype=im['nomensetpodtype'])
                                nomen_sets.append(nomen_set.id)
                            else:
                                nomen_sets.append(NomenSet.objects.get(guid=im['guid']).id)

                    # Загрузка полей, которые ссылаются на себя

                    analogs = []
                    addprods = []

                    if item['analogs'] != '':
                        for im in item['analogs']:
                            if Set.objects.filter(guid=im['guid']).exists():
                                analogs.append(Set.objects.get(guid=im['guid']).id)
                            else:
                                print('Set_1 попался, точнее не нашелся! guid=', im['guid'])

                    if item['addprods'] != '':
                        for im in item['addprods']:
                            if Set.objects.filter(guid=im['guid']).exists():
                                addprods.append(Set.objects.get(guid=im['guid']).id)
                            else:
                                print('Set_2 попался, точнее не нашелся!guid=', im['guid'])

                    set = Set.objects.create(guid=guid, name=name, article=article, description=description,
                                             smallsize=smallsize, composition=composition,
                                             length=length, width=width, height=height, weight=weight,
                                             mainprice=mainprice, subprodtype=subprodtype,
                                             collection=collection, brand=brand, manufacturer=manufacturer,
                                             is_new=is_new, is_hit=is_hit, is_mainphoto=is_mainphoto,
                                             is_set=is_set, is_sale=is_sale, maintenance=maintenance,
                                             gender_type=gender_type)
                    if images:
                        set.images.add(*images)
                    if analogs:
                        set.analogs.add(*analogs)
                    if addprods:
                        set.addprods.add(*addprods)
                    if nomen_sets:
                        set.nomen_sets.add(*nomen_sets)


def get_images(im_item: dict) -> list:
    images = []
    for im in im_item['images']:
        if not Image.objects.filter(imagename=im['imagename']).exists():
            image = Image(imagename=im['imagename'], guid=im['guid'],
                          imagesize=im['imagesize'],
                          imageext=im['imageext'],
                          imagemask=im['imagemask'],
                          imagetype=im['imagetype'],
                          imagesubtype=im.get('imagesubtype', None))
            try:
                image.save()
            except Exception as e:
                print(e.__str__())
                return

            images.append(image.id)
        else:
            images.append(Image.objects.get(imagename=im['imagename']).id)
    return images


def load_all():
    load_sub_tables()
    load_characteristics()
    load_products()
    load_sets()
