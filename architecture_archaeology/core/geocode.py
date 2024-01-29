import requests
import architecture_archaeology.settings as settings
from decimal import Decimal
from pprint import pprint

def create_geocode_url(long, lat):
    if not isinstance(long, (Decimal, float)) and not isinstance(lat, (Decimal, float)):
        raise ValueError('Not a decimal value')
    url = f'https://geocode-maps.yandex.ru/1.x?apikey={settings.YMAPS_TOKEN}&geocode={long}, {lat}&lang=ru_RU&format=json'
    return url


def get_location_data(url):
    resp = requests.get(url).json()
    print(resp)
    # for i in resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']:
    #     print(i)
    print('------------')
    # print(resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'])
    # return resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
    # try:
    #     address_data = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
    #     region_data = {
    #         "country": address_data[0]['name'],
    #         "region": address_data[2]['name'],
    #         "rayon": address_data[3]['name'],
    #         "locality": address_data[-1]['name']
    #     }
    #     # print(region_data)
    # except:
    #     print(resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'])
