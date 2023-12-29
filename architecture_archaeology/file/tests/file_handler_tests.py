from file.services import FileHandler
from core.tests import BaseTestCreateView
from arch_site.models import ArchaeologicalSite
from helpers.models import Region


class FileHandlerTest(BaseTestCreateView):
    fixtures = ['countries.json',
                'regions.json',
                'filetypes.json'
                ]

    def setUp(self):
        self.files = self.image_files_factory(1)
        self.site = ArchaeologicalSite.objects.create(name='Test name', long=1, lat=1, region=Region.objects.last())

    def test_invalid_file(self):
        with self.assertRaises(ValueError):
            FileHandler('test', 'another_test', 'ftype')

    def test_correct_data(self):     
        file = FileHandler(self.files[0], self.site, 'фотография')
        self.assertEqual(file.object_storage_key, f'arch_site_archaeologicalsite/{self.site.pk}/{file.filename}')

    def test_invalid_ftype(self):
        with self.assertRaises(ValueError):
            FileHandler(self.files[0], self.site, 'ftype')

    def test_invalid_parent(self):
        with self.assertRaises(ValueError):
            FileHandler(self.files[0], 'another_test', 'фотография')
    
    def test_url(self):
        pass

    def test_form_valid(self):
        pass
