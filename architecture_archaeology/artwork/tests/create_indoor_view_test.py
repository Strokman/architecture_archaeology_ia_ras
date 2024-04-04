from django.test import TestCase, Client
from django.urls import reverse_lazy

from artwork.models import IndoorArtwork


class CreateIndoorViewTest(TestCase):
    client = Client()
    fixtures = ['arch_sites.json',
                'colors.json',
                'preservations.json'
                ]
    
    def setUp(self) -> None:
        self.url = reverse_lazy('artwork:submit-indoorartwork')
        self.payload = {
            'site': 1,
            'preservation': 1
        }

    def test_view(self):
        resp = self.client.get(reverse_lazy('artwork:submit-indoorartwork'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['action'], reverse_lazy('artwork:submit-indoorartwork'))

    def test_artwork_created(self):
        resp = self.client.post(self.url, data=self.payload, follow=True)
        obj = IndoorArtwork.objects.get(id=1)
        self.assertEqual(obj.code, 1)
        self.assertEqual(resp.status_code, 200)