import architecture_archaeology.settings as settings
from django.test import TestCase
from csv import DictReader
from core.geocode import create_geocode_url, get_location_data
from decimal import Decimal


class GeocodeTest(TestCase):
    
    def test_coords(self):
        with open(f'{settings.BASE_DIR}/static/test_coords.csv', 'r', encoding="utf-8-sig") as f:
            data = DictReader(f, delimiter=';')
            counter = 0
            
            for column in data:
                while counter < 100:
                    long = Decimal(column['long'])
                    lat = Decimal(column['lat'])
                    data = get_location_data(create_geocode_url(long, lat))
                    print('country' in data)
                    counter += 1
                    break
