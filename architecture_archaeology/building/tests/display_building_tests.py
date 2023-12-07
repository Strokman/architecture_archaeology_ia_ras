from django.test import TestCase, Client
from django.urls import reverse

from building.models import Building


class DisplayBuildingViewTest(TestCase):
    client = Client()

    def test_no_building(self):
        resp = self.client.get(reverse('building:display'))
        self.assertEqual(resp.status_code, 404)

    def test_building_created(self):
        self.model = Building.objects.create(name='Test name', description='test desc', long=12, lat=13)
        resp = self.client.get(reverse('building:display'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['building'], self.model)

