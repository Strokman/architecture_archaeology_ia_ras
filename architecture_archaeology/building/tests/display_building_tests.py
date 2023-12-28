from django.test import TestCase, Client
from django.urls import reverse

from building.models import Building


class DisplayBuildingViewTest(TestCase):
    client = Client()
    fixtures = ['countries.json', 'regions.json', 'arch_sites.json', 'buildings.json']

    def setUp(self):
        self.building = Building.objects.last()

    def test_no_building(self):
        self.building.delete()
        resp = self.client.get(reverse('building:display', kwargs={'slug': self.building.slug}))
        self.assertEqual(resp.status_code, 404)

    def test_display_building(self):
        resp = self.client.get(reverse('building:display', kwargs={'slug': self.building.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_context(self):
        resp = self.client.get(reverse('building:display', kwargs={'slug': self.building.slug}))
        self.assertIn(self.building.name, resp.context['title'])

