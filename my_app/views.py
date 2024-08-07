from importlib.abc import Loader
from webbrowser import get

from django.core.validators import URLValidator
from rest_framework.exceptions import ValidationError

from models import *
from rest_framework.views import APIView
from django.http import JsonResponse

import yaml


def load_yaml(yaml_data):
    """
    Функция для загрузки данных из строки в формате YAML.
    Преобразует их в словарь.

    :param yaml_data: Строка с данными в формате YAML.
    :return: Словарь с данными, преобразованными из YAML.
    """
    try:
        # Используем yaml.safe_load для безопасной загрузки данных
        data = yaml.safe_load(yaml_data)
    except yaml.YAMLError as exc:
        print(f"Ошибка при загрузке YAML: {exc}")
        raise
    return data

data = load_yaml(shop1.yaml)
print(data)


class PartnerUpdate(APIView):
    """
    Класс для обновления прайса от поставщика
    """
    def post(self, request, *args, **kwargs):

        # Проверка аутентификации пользователя.
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)

        # Проверка типа пользователя.
        if request.user.type != 'shop':
            return JsonResponse({'Status': False, 'Error': 'Только для магазинов'}, status=403)

        # Валидация URL.
        url = request.data.get('url')
        if url:
            validate_url = URLValidator()
            try:
                validate_url(url)
            except ValidationError as e:
                return JsonResponse({'Status': False, 'Error': str(e)})
            else:
                stream = get(url).content

                data = load_yaml(stream, Loader=Loader)

                # Загрузка данных по URL
                shop, _ = Shop.objects.get_or_create(name=data['shop'], user_id=request.user.id)

                # Загруженные данные используются для создания или обновления записей в базе данных.
                for category in data['categories']:
                    category_object, _ = Category.objects.get_or_create(id=category['id'], name=category['name'])
                    category_object.shops.add(shop.id)
                    category_object.save()
                ProductInfo.objects.filter(shop_id=shop.id).delete()
                for item in data['goods']:
                    product, _ = Product.objects.get_or_create(name=item['name'], category_id=item['category'])

                    product_info = ProductInfo.objects.create(product_id=product.id,
                                                              external_id=item['id'],
                                                              model=item['model'],
                                                              price=item['price'],
                                                              price_rrc=item['price_rrc'],
                                                              quantity=item['quantity'],
                                                              shop_id=shop.id)
                    for name, value in item['parameters'].items():
                        parameter_object, _ = Parameter.objects.get_or_create(name=name)
                        ProductParameter.objects.create(product_info_id=product_info.id,
                                                        parameter_id=parameter_object.id,
                                                        value=value)

                return JsonResponse({'Status': True})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})

