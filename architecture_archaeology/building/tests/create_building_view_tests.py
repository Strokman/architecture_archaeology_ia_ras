from django.test import TransactionTestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile, SimpleUploadedFile

from PIL import Image
from io import BytesIO


from building.models import Building
from building.forms import SubmitBuildingForm

from core.tests import BaseTestCreateView


class CreateBuildingViewTest(BaseTestCreateView):
    model = Building
    fixtures = ['countries.json',
                'regions.json',
                'arch_sites.json',
                'filetypes.json'
                ]
    form = SubmitBuildingForm
    
    def setUp(self):
        self.files = self.image_files_factory(6)
        self.payload = {
                'name': 'Церковь Покрова не Нерли',
                'long': 55.9,
                'lat': 60.88,
                'description': 'test-description',
                'site': 1
                }
        self.url = reverse('building:submit')

    def test_building_created(self):
        response = self.client.post(self.url, data=self.payload, follow=True)
        self.assertRedirects(response, '/')
        self.assertEqual(Building.objects.count(), 1)
        self.assertEqual(Building.objects.last().name, self.payload['name'])

        payload = {
            'name': 123,
            'long': '22',
            'lat': 44.5,
            'site': '1'
        }
        response = self.client.post(self.url, data=payload, follow=True)
        self.assertRedirects(response, '/', status_code=302, fetch_redirect_response=False)
        self.assertEqual(Building.objects.count(), 2)
        self.assertEqual(Building.objects.last().name, str(payload['name']))

    def test_building_not_created(self):
        payload = {
            'name': 123,
            'long': 'qwerty',
            'lat': 44.5,
            'site': '1'
        }
        response = self.client.post(self.url, data=payload, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Building.objects.count(), 0)
        payload = {
            'name': 123,
            'long': 'qwerty',
            'lat': 4455.5,
            'site': '1'
        }
        response = self.client.post(self.url, data=payload, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Building.objects.count(), 0)

    def test_file(self):
        counter = 0
        for file in self.files:
            self.payload['foto'] = file
            response = self.client.post(self.url, data=self.payload, follow=True)
            if self.payload['foto'].name.endswith('.jpeg'):
                counter += 1
                self.assertRedirects(response, '/')
                self.assertEqual(Building.objects.count(), counter)
                self.assertEqual(Building.objects.last().name, self.payload['name'])
            else:
                self.assertEqual(Building.objects.count(), counter)
