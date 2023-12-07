from django.test import TestCase
from django.utils.text import slugify
from django.db.utils import DataError
from django.core.exceptions import ValidationError

from building.models import Building
from helpers.models import Region


# Create your tests here.
class BuildingModelTest(TestCase):
    fixtures = ['countries.json', 'regions.json']

    buildings_names = ['Церковь Спаса на Нередице', 'Церковь Покрова не Нерли', 'Георгиевский собор Юрьева монастыря']

    def setUp(self) -> None:
        self.region = Region.objects.get(name__contains='Новгородская')
        self.buildings = {}
        self.description = 'test description'
        for name in self.buildings_names:
            building = Building.objects.create(name=name, description=self.description, long=45.55, lat=55.45, region=self.region)
            self.buildings[name] = building

    def test_building_creation(self):
        for k, v in self.buildings.items():
            self.assertEqual(v.long, 45.55)
            self.assertEqual(v.lat, 55.45)
            self.assertEqual(v.name, k)
            self.assertEqual(v.region, self.region)
            self.assertEqual(v.slug, slugify(k))
            self.assertEqual(str(v), k)

    def test_get_url(self):
        for k, v in self.buildings.items():
            self.assertEqual(v.get_url(), v.slug)

    def test_building_deletion(self):
        for k, v in self.buildings.items():
            v.delete()
            with self.assertRaises(Building.DoesNotExist): 
                Building.objects.get(id=v.id)

    def test_max_length_name(self):
        with self.assertRaises(DataError):
            Building.objects.create(name=''.join(['a' for i in range(300)]), description=self.description, long=45.55, lat=55.45, region=self.region)

    def test_incorrect_data_types(self):
        with self.assertRaises(ValidationError):
            Building.objects.create(name='Test', description=self.description, long='qwerty', lat='60', region=self.region)
        with self.assertRaises(ValueError):
            Building.objects.create(name='Test', description=self.description, long=50, lat=50, region='test')
