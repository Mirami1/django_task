from .models import *
import json
from django.apps import apps
import logging


logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)

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
"""Влезаем в файл, вытаскиваем необходимый класс из словаря моделей, создаем обьект модели и заполнем по-строково
 его поля, картинки, если есть, загружаются в отдельном методе, добавляем ключи 
 от картинок в соответствующее поле и в конце сохраняем обьект"""


def load_sub_tables():
    logging.info('ЗАГРУЗКА ДОПТАБЛИЦ')

    directories_models = apps.all_models['products']
    with open('get_directories.json', 'r', encoding='UTF-8') as json_file:
        data = json.load(json_file)
        for type in data['models']:
            str = type['model'].lower().strip().replace('с', 'c')
            logging.info(str)
            model_class = directories_models.get(str)

            for item in type['items']:
                obj = model_class()
                for key, value in item.items():
                    try:
                        if key == 'images' and value:
                            logging.info('image')
                            obj.save()
                            obj.images.set(load_images(value))
                            continue
                        elif key != 'images':
                            setattr(obj, key, value)
                    except Exception as e:
                        logging.exception('Exception occurred')
                        return
                    obj.save()


# получаем словарь картинок, потом как по списку проходимся, заполняем и сохраняем картинку,
# если его нет в таблице с картинками, в обоих случаем сохраняем id
def load_images(im_dict: dict) -> list:
    images = []
    for im in im_dict:
        if not Image.objects.filter(guid=im['guid']).exists():
            image = Image()
            for key, value in im.items():
                setattr(image, key, value)
            try:
                image.save()
            except Exception as e:
                logging.exception('Exception occurred')
                return

            images.append(image.id)
        else:
            images.append(Image.objects.get(guid=im['guid']).id)
    return images


# Загрузка таблиц с характеристиками, товарами и наборами
"""Здесь всё по-сложнее принцип примерно такой же, но прибавляеются уже костыли, некоторые поля необходимо переименовывать чтобы совпадало с моделью из БД,
также различаем значения полей - поле может быть строкой или списком, если строка, то простой, или ключом для ссылки на другой обьект
 если строка, то добавляем как атрибут к обьекту,
 если строка, то ключ ссылается на другую таблицу, находим по guid/создаем id обьекта и добавляем id обьекта как поле для внешнего ключа,
 если это список, то такое поле имеет тип многие-ко-многим, проходимся по списку, проверяем является ли элемент списка словарем или строкой, 
 также создаем специальный словарь для хранения idшников по ссылочным полям для удобства,
 если строка, то находим по guid idшники и кидаем в список,
 если словарь, то проверяем по guid /создаем обьект, idшники тоже кидаем в список,
 в конце сейвим обьект и заполняем поля многие-ко-многим,
 потом еще раз проходимся по всем обьектам типа, но уже для заполениния двух полей типа многие-ко-многим, которые ссылаются сами на себя"""


def load_characteristics():
    logging.info('ЗАГРУЗКА ОСНОВНЫХ ТАБЛИЦ')

    directories_models = apps.all_models['products']  # словарь всех конструкторов моделей приложения
    with open('get_products.json', 'r', encoding='UTF-8') as json_file:
        data = json.load(json_file)
        for type in data['models']:
            str = type['model'].lower().strip()
            logging.info(str)
            model_class = directories_models.get(str)

            for item in type['items']:
                obj = model_class()
                many_to_many = {}  # словарь которые хранит idшники полей многие-ко-многим
                for key, value in item.items():
                    try:
                        # костыли с названиями
                        if key == 'brand':
                            key += 's'
                        if key == 'prodtypes':
                            key = 'typemodels'
                        if key == 'desings':
                            key = 'designs'
                        if key == 'nomen_sets':
                            key = 'nomensets'

                        # является ли название поля моделью и значение не является ли списком
                        if key in directories_models and value is not list:
                            if directories_models[key].objects.filter(guid=value).exists():
                                fk_obj = directories_models[key].objects.get(guid=value)
                            else:
                                fk_obj = None
                            setattr(obj, key, fk_obj)
                            continue

                        # если значение является списком
                        if isinstance(value, list):
                            if key == 'analogs' or key == 'addprods':  # избегаем ссылающихся сами на себя полей
                                continue
                            many_to_many[key] = []
                            # проходимся по списку
                            for item_1 in value:
                                if len(item_1) == 1:
                                    for key_1, value_1 in item_1.items():
                                        if directories_models[key[:-1]].objects.filter(guid=value_1).exists():
                                            many_to_many[key].append(
                                                directories_models[key[:-1]].objects.get(guid=value_1).id)
                                else:
                                    obj_1 = directories_models[key[:-1]]()
                                    creation = False
                                    for key_1, value_1 in item_1.items():
                                        if directories_models[key[:-1]].objects.filter(guid=value_1).exists():
                                            many_to_many[key].append(
                                                directories_models[key[:-1]].objects.get(guid=value_1).id)
                                            break
                                        else:
                                            setattr(obj_1, key_1, value_1)
                                            creation = True
                                    if creation:  # создавался ли обьект (словарь имел длину больше 1?)
                                        try:
                                            obj_1.save()
                                        except Exception as e:
                                            logging.exception('Exception occurred')
                                            return
                                        many_to_many[key].append(obj_1.id)

                            continue
                        # если поле строковое
                        if not isinstance(value, list):
                            if key == 'is_mainfoto':  # костыль из-за фотки
                                if Image.objects.filter(guid=value).exists():
                                    setattr(obj, key, Image.objects.get(guid=value).id)
                            else:
                                setattr(obj, key, value)  # добавляем простое поле
                    except Exception as e:
                        logging.error(key, value)
                        logging.exception('Exception occurred')
                        return
                obj.save()

                # проходимся по словару с idшниками ссылющихся таблиц и добавляем idшники к полям многие-ко-многим
                for key_2, value_2 in many_to_many.items():
                    if value_2:
                        if key_2 == 'typemodels':
                            key_2 = 'prodtypes'
                            getattr(obj, key_2).add(*value_2)
                        elif key_2 == 'nomensets':
                            key_2 = 'nomen_sets'
                            getattr(obj, key_2).add(*value_2)

                        else:
                            getattr(obj, key_2).add(*value_2)

            # проходимся снова по обьектам модели в поиске ссылающихся на себя полей
            for item in type['items']:
                existed_obj = model_class.objects.get(guid=item['guid'])
                many_to_many = {'analogs': [], 'addprods': []}
                for key, value in item.items():
                    if key == 'addprods' or key == 'analogs':
                        if value:
                            for value_1 in value:
                                if model_class.objects.filter(guid=value_1['guid']).exists():
                                    many_to_many[key].append(
                                        model_class.objects.get(guid=value_1['guid']).id)
                                    continue

                for key_3, value_3 in many_to_many.items():
                    if value_3:
                        getattr(existed_obj, key_3).add(*value_3)


def load_all():

    load_sub_tables()
    load_characteristics()
