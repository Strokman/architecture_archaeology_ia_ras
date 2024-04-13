from django.test import TestCase

from arch_site.models import ArchaeologicalSite, ArchSiteFoto
from helpers.models import Region, Country
from file.services.file_factory import FileFactory


class FileFactoryTest(TestCase):

    def setUp(self) -> None:
        country = Country.objects.create(name='Россия')
        region = Region.objects.create(name='Московская область', country=country)
        self.site = ArchaeologicalSite.objects.create(
                                                    name='Test name',
                                                    long=55.693975,
                                                    lat=37.305412,
                                                    region=region
                                                    )
        self.foto = {
            'filename': 'test_filename',
            'extension': 'pdf',
            'original_name': 'some random name',
            'object_storage_key': 'key'

        }


    def test_file_creation(self):
        file = FileFactory.create_file('foto', self.foto)
        self.assertEqual(file.filename, self.foto['filename'])



        # for i in range(10):
        #     filename = f'filename{i}'
        #     orig_fname = f'orig_filename{i}'
        #     foto = Foto.objects.create(
        #         filename=filename,
        #         extension='pdf',
        #         original_name=orig_fname,
        #         object_storage_key=f'arch_site/{self.sites[i % 2].pk}/{filename}'
        #     )
        #     self.fotos.append(foto)
        #     ArchSiteFoto.objects.create(site=self.sites[i % 2], foto=foto)
        # self.table = ArchSiteFoto.objects.all()