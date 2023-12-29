from django.test import TransactionTestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile, SimpleUploadedFile

from PIL import Image
from io import BytesIO


from building.models import Building
from building.forms import SubmitBuildingForm


class CreateBuildingViewTest(TransactionTestCase):
    client = Client()
    fixtures = ['countries.json',
                'regions.json',
                'arch_sites.json',
                'filetypes.json']

    def setUp(self):
        self.files = self.files_factory(6)
        file = BytesIO()
        image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        self.incorrect_image = file
        # SimpleUploadedFile(
        #     'random-incorrect-name.jpg', b'contetn', 'image/jpeg'
        # )
        self.form = SubmitBuildingForm
        self.building = {
                'name': 'Церковь Покрова не Нерли',
                'long': 55.9,
                'lat': 60.88,
                'description': 'test-description',
                'site': 1
                }
        self.url = reverse('building:submit')

    def files_factory(self, amount):
        files = []
        extensions = ['jpeg', 'tiff']
        for i in range(amount):
            im = Image.new(mode='RGB', size=(200, 200)) # create a new image using PIL
            im_io = BytesIO() # a BytesIO object for saving image
            im.save(im_io, f'{extensions[i % 2].upper()}') # save the image to im_io
            im_io.seek(0) # seek to the beginning
            files.append(InMemoryUploadedFile(
            im_io, None, f'random-name.{extensions[i % 2]}', f'image/{extensions[i % 2]}', len(im_io.getvalue()), None
        ))
        return files

    def test_url(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Добавление', resp.context['title'])

    def test_form_valid(self):
        form = self.form(data=self.building)
        self.assertTrue(form.is_valid())
        form = self.form(data={'name': 'test-name'})
        self.assertFalse(form.is_valid())

    def test_building_created(self):
        response = self.client.post(self.url, data=self.building, follow=True)
        self.assertRedirects(response, '/')
        self.assertEqual(Building.objects.count(), 1)
        self.assertEqual(Building.objects.last().name, self.building['name'])

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
            self.building['foto'] = file
            response = self.client.post(self.url, data=self.building, follow=True)
            if self.building['foto'].name.endswith('.jpeg'):
                counter += 1
                self.assertRedirects(response, '/')
                self.assertEqual(Building.objects.count(), counter)
                self.assertEqual(Building.objects.last().name, self.building['name'])
            else:
                self.assertEqual(Building.objects.count(), counter)
