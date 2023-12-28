from django.core.management.base import BaseCommand
from architecture_archaeology.settings import BASE_DIR
from csv import DictReader
from building.models import Building
from arch_site.models import ArchaeologicalSite

import random
from core.utils import slugify


class Command(BaseCommand):
    help = "Создает записи для построек в базе данных"

    def handle(self, *args, **options):

        with open(f'{BASE_DIR}/pre_defined_data/buildings.csv', 'r', encoding='utf-8-sig') as f:
            row = DictReader(f, delimiter=';')
            lst = []
            for column in row:
                site = ArchaeologicalSite.objects.get(name=column['site']).pk
                del column['site']
                column['site_id'] = site
                for k in column:
                    if not column[k]:
                        column[k] = None
                column['slug'] = slugify(column['name'], allow_unicode=True) + '-' + str(random.randint(10, 10000))
                lst.append(Building(**column))
        Building.objects.bulk_create(lst)
        print('Buildings created')
