from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Filler


class Command(BaseCommand):
    help = "Создает записи для заполнителей в базе данных"

    def handle(self, *args, **options):
        fillers = Filler.objects.all()
        if not fillers:
            with open(f'{BASE_DIR}/pre_defined_data/fillers.txt', 'r') as f:
                data = f.read().split('\n')
                lst = []
                for row in data:
                    
                    lst.append(Filler(description=row))
            Filler.objects.bulk_create(lst)
            print('Fillers created')
        else:
            raise CommandError('Fillers already created')