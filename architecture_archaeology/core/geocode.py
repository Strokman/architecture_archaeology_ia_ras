import requests
import architecture_archaeology.settings as settings
from decimal import Decimal


"""
Для получения и присвоения географической принадлежности объектов используется
API Яндекс карт. Ключ для API привязан к аккаунту яндекса лаборатории (также и сервер в облаке у них).
"""

def create_geocode_url(lat, long):
    # Функция создает ссылку для запроса по координатам
    if not isinstance(long, (Decimal, float)) and not isinstance(lat, (Decimal, float)):
        raise ValueError('Not a decimal value')
    url = f'https://geocode-maps.yandex.ru/1.x?apikey={settings.YMAPS_TOKEN}&geocode={long}, {lat}&lang=ru_RU&format=json'
    return url


def get_location_data(url):
    """
    Функция делает запрос к API Яндекс Карт (геокод).
    Проверяется, есть ли необходимые данные в ответе:
    Страна и административная единица (облась, край и т.п.)
    Например, если пользователь введет координаты в море - 
    то данных не будет и функция выдаст ошибку. Пользователь
    должен будет ввести корректные координаты.
    """
    try:
        resp = requests.get(url).json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
        region_data = {}
        for i in resp:
            match i['kind']:
                case 'country':
                    region_data['country'] = i['name']
                case 'province':
                    region_data['region'] = i['name']
                case 'area' if 'region' not in region_data:
                    region_data['region'] = i['name']
                case 'locality' if 'region' not in region_data:
                    region_data['region'] = i['name']
        if not region_data:
            raise ValueError('Неверные координаты')
        return region_data
    except IndexError:
        raise ValueError('Неверные координаты')
