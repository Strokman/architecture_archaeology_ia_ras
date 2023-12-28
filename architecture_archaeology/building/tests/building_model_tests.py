from django.test import TransactionTestCase
from django.db.utils import DataError, IntegrityError
from django.core.exceptions import ValidationError

from building.models import Building
from arch_site.models import ArchaeologicalSite


# Create your tests here.
class BuildingModelTest(TransactionTestCase):
    fixtures = ['countries.json', 'regions.json', 'arch_sites.json']
    buildings = {}

    buildings_names = ['Церковь Спаса на Нередице', 'Церковь Покрова не Нерли', 'Георгиевский собор Юрьева монастыря', 'Церковь Спаса на Нередице']

    def setUp(self) -> None:
        self.site = ArchaeologicalSite.objects.last()
        self.description = 'test description'
        for name in self.buildings_names:
            building = Building.objects.create(name=name, description=self.description, long='45.55', lat=55.45, site=self.site)
            self.buildings[name] = building

    def test_building_creation(self):
        buildings = Building.objects.all()
        for v in range(len(buildings)):
            self.assertEqual(float(round(buildings[v].long, 2)), 45.55)
            self.assertEqual(float(round(buildings[v].lat, 2)), 55.45)
            self.assertEqual(buildings[v].name, self.buildings_names[v])
            self.assertEqual(str(buildings[v]), self.buildings_names[v])
            self.assertEqual(buildings[v].site, self.site)

    def test_slug(self):
        buildings = []
        slug = 'test-string'
        for name in self.buildings_names:
            buildings.append(Building(name=name, description=self.description, long=45, lat=56, slug=slug, site=self.site))
        with self.assertRaises(IntegrityError):
            Building.objects.bulk_create(buildings)

    def test_building_deletion(self):
        for k, v in self.buildings.items():
            v.delete()
            with self.assertRaises(Building.DoesNotExist): 
                Building.objects.get(id=v.id)

    def test_max_length_name(self):
        with self.assertRaises(DataError):
            Building.objects.create(name=''.join(['a' for i in range(300)]), description=self.description, long=45.55, lat=55.45, site=self.site)
    
    def test_incorrect_long_lat(self):
        with self.assertRaises(DataError):
            Building.objects.create(name='Test', long=1234.223456789876543210987663121212, lat=55.5, site=self.site)

    def test_incorrect_data_types(self):
        with self.assertRaises(ValidationError):
            Building.objects.create(name='Test', description=self.description, long='50.55', lat='иии', site=self.site)
            Building.objects.create(name='Test', description=self.description, long=50, lat='60.a', site=self.site)
        with self.assertRaises(IntegrityError):
            Building.objects.create(name='Test', description=self.description, long=50, lat=50)
        with self.assertRaises(ValueError):
            Building.objects.create(name='Test', description=self.description, long=50, lat=50, site='test')
