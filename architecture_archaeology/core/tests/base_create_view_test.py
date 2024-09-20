from io import BytesIO

from PIL import Image
from django.test import TestCase, Client
from django.core.files.uploadedfile import InMemoryUploadedFile


class BaseTestCreateView(TestCase):
    client = Client()

    # def test_url(self):
    #     resp = self.client.get(self.url)
    #     self.assertEqual(resp.status_code, 302)
    #     self.assertIn('Добавление', resp.context['title'])

    def image_files_factory(self, amount=10):
        files = []
        extensions = ['jpeg', 'tiff', 'png', 'gif']
        for i in range(amount):
            im = Image.new(mode='RGB', size=(200, 200)) # create a new image using PIL
            im_io = BytesIO() # a BytesIO object for saving image
            im.save(im_io, f'{extensions[i % 2].upper()}') # save the image to im_io
            im_io.seek(0) # seek to the beginning
            files.append(
                InMemoryUploadedFile(
                                    im_io,
                                    None,
                                    f'random-name.{extensions[i % 2]}',
                                    f'image/{extensions[i % 2]}',
                                    len(im_io.getvalue()),
                                    None
                                    ))
        return files

    # def test_form_valid(self):
    #     form = self.form(data=self.payload)
    #     self.assertTrue(form.is_valid())
    #     form = self.form(data={'name': 'test-name'})
    #     self.assertFalse(form.is_valid())
