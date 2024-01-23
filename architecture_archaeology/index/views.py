from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View
import requests
import pprint
import architecture_archaeology.settings as settings



class IndexView(View):
    pass


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'text': 'placeholder'
    }
    resp = requests.get(f'https://geocode-maps.yandex.ru/1.x?apikey={settings.YMAPS_TOKEN}&geocode=140.727552, 38.170710&lang=ru_RU&format=json').json()
    # pprint.pprint(resp.json())
    # pprint.pprint(resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'])
    if resp['response']['GeoObjectCollection']['featureMember']:

        address_data = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
        country = address_data[0]['name']
        region = address_data[2]['name']
        rayon = address_data[3]['name']
        locality = address_data[-1]['name']
        print(country)
        print(region)
        print(rayon)
        print(locality)
    else:
        print('Где то в небытии')
    return HttpResponse(template.render(context, request))
