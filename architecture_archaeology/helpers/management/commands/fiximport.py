from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Storage, Color
from building.models import Building
from arch_site.models import ArchaeologicalSite
from artwork.models import Frescoe
from csv import DictReader
from core.services.index_service import sequence_id


class Command(BaseCommand):
    help = "Фикс записей с постройками"

    def handle(self, *args, **options):
        with open(f'{BASE_DIR}/pre_defined_data/frescoes_main.csv', 'r', encoding='utf-8-sig') as f:
            data = DictReader(f, delimiter=';')
            
            for row in data:
                
                if row['№']:
                    if not row['Постройка']:
                        frescoe = Frescoe.objects.get(code=row['№'])
                        print(frescoe)
                        # frescoe.save()
