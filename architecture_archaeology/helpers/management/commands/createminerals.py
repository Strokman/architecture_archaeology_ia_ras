from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Mineral


class Command(BaseCommand):
    help = "Создает записи для минералов в базе данных"

    def handle(self, *args, **options):
        minerals = Mineral.objects.all()
        if not minerals:
            with open(f'{BASE_DIR}/pre_defined_data/minerals.txt', 'r') as f:
                data = f.read().split('\n')
                lst = []
                for row in data:
                    if row:
                        lst.append(Mineral(description=row))
            Mineral.objects.bulk_create(lst)
            print('Minerals created')
        else:
            raise CommandError('Minerals already created')