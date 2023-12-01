from django.test import TestCase
from django.utils.text import slugify

from building.models import Building
from helpers.models import Region


# Create your tests here.
class BuildingModelTest(TestCase):
    fixtures = ['countries.json', 'regions.json']

    buildings_names = ['Церковь Спаса на Нередице', 'Церковь Покрова не Нерли', 'Георгиевский собор Юрьева монастыря']

    def setUp(self) -> None:
        self.region = Region.objects.get(name__contains='Новгородская')
        self.buildings = {}
        for name in self.buildings_names:
            building = Building.objects.create(name=name, long=45.55, lat=55.45, region=self.region)
            self.buildings[name] = building

    def test_building_creation(self):
        for k, v in self.buildings.items():
            self.assertEqual(v.long, 45.55)
            self.assertEqual(v.lat, 55.45)
            self.assertEqual(v.name, k)
            self.assertEqual(v.region, self.region)
            self.assertEqual(v.slug, slugify(k))
