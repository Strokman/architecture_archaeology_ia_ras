from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from building.models import BuildingPart


class Command(BaseCommand):
    help = "Создает записи для элементов построек в базе данных"

    def handle(self, *args, **options):
        building_parts = BuildingPart.objects.all()
        if not building_parts:
            with open(f'{BASE_DIR}/pre_defined_data/building_parts.txt', 'r') as f:
                data = f.read().split('\n')
                lst = []
                for row in data:
                    if row:
                        lst.append(BuildingPart(name=row))
            BuildingPart.objects.bulk_create(lst)
            print('Building parts created')
        else:
            raise CommandError('Building parts already created')
