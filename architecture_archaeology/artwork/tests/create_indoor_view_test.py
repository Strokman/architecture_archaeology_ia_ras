from django.test import TestCase, Client
from django.urls import reverse_lazy

from artwork.models import IndoorArtwork


class CreateIndoorViewTest(TestCase):
    client = Client()

    def test_view(self):
        resp = self.client.get(reverse_lazy('artwork:submit-indoorartwork'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['action'], reverse_lazy('artwork:submit-indoorartwork'))

    def test_artwork_created(self):
        params = {
            'name': 'Some random test name for artwork',
            'year_min': 111,
            'year_max': '222',
        }
        self.model = IndoorArtwork.objects.create(name='Test name', description='test desc', long=12, lat=13)
        resp = self.client.get(reverse_lazy('building:display'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['building'], self.model)