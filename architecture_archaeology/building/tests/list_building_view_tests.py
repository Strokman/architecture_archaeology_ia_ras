from django.test import TransactionTestCase, Client
from django.urls import reverse

from building.models import Building
from arch_site.models import ArchaeologicalSite
from building.views import BuildingListView


class ListBuildingViewTest(TransactionTestCase):
    client = Client()
    fixtures = ['countries.json',
                'regions.json',
                'arch_sites.json',
                'buildings.json']

    def setUp(self):
        self.view = BuildingListView()
        self.url = reverse('building:list')
        self.site = ArchaeologicalSite.objects.last()

    def test_url(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Постройки', resp.context['title'])

    def test_queryset(self):
        qset = self.view.get_queryset()
        self.assertEqual(len(qset), 4)

    def test_building_added(self):
        qset = self.view.get_queryset()
        Building.objects.create(name='test', long=1, lat=2, site=self.site)
        self.assertEqual(len(qset), 5)

    def test_building_deleted(self):
        bld = Building.objects.last()
        bld.delete()
        qset = self.view.get_queryset()
        self.assertEqual(len(qset), 3)
