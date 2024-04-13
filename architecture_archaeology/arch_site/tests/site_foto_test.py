from django.test import TestCase

from arch_site.models import ArchaeologicalSite, ArchSiteFoto
from helpers.models import Region, Country
from file.models import Foto


class ArchSiteFotoTest(TestCase):

    def setUp(self) -> None:
        country = Country.objects.create(name='Россия')
        region = Region.objects.create(name='Московская область', country=country)
        self.sites = []
        for i in range(2):
            site = ArchaeologicalSite.objects.create(
                                                    name=f'Test name{i}',
                                                    long=55.693975,
                                                    lat=37.305412,
                                                    region=region
                                                    )
            self.sites.append(site)
        self.fotos = []
        for i in range(10):
            filename = f'filename{i}'
            orig_fname = f'orig_filename{i}'
            foto = Foto.objects.create(
                filename=filename,
                extension='pdf',
                original_name=orig_fname,
                object_storage_key=f'arch_site/{self.sites[i % 2].pk}/{filename}'
            )
            self.fotos.append(foto)
            ArchSiteFoto.objects.create(site=self.sites[i % 2], foto=foto)
        self.table = ArchSiteFoto.objects.all()

    def test_intermediate_table(self):
        self.assertEqual(len(self.table), 10)
        site = self.sites[0]
        foto = Foto.objects.filter(archsitefoto__site_id=site.pk)
        for i in range(len(foto)):
            self.assertEqual(foto[i], site.archsitefoto_set.all()[i].foto)
