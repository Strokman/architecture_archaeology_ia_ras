from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Material


class Command(BaseCommand):
    help = "Создает записи для материалов в базе данных"

    def handle(self, *args, **options):
        materials = Material.objects.all()
        if not materials:
            with open(f'{BASE_DIR}/pre_defined_data/filler.txt', 'r') as f:
                materials = f.read().split('\n')
                lst = []
                for pigment in materials:
                    lst.append(Material(description=pigment))
            Material.objects.bulk_create(lst)
            print('materials created')
        else:
            raise CommandError('materials already created')