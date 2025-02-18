from django.core.management.base import BaseCommand
from architecture_archaeology.settings import BASE_DIR
from csv import DictReader
from arch_site.models import ArchaeologicalSite

import random
from core.utils import slugify



class Command(BaseCommand):
    """
    Команда использовалась для загрузки данных о памятниках
    из файла, предоставленного Лабораторией архитектурной археологии
    """
    help = "Создает записи для археологических памятников в базе данных"

    def handle(self, *args, **options):

        with open(f'{BASE_DIR}/pre_defined_data/arch_sites.csv', 'r', encoding='utf-8-sig') as f:
            row = DictReader(f, delimiter=';')
            lst = []
            for column in row:
                for k in column:
                    if not column[k]:
                        column[k] = None
                column['region_id'] = 1
                column['slug'] = slugify(column['name'], allow_unicode=True) + '-' + str(random.randint(10, 10000))
                lst.append(ArchaeologicalSite(**column))
        ArchaeologicalSite.objects.bulk_create(lst)
        print('Archaeological sites created')