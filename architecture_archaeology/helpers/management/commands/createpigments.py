from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Pigment


class Command(BaseCommand):
    help = "Создает записи для пигментов в базе данных"

    def handle(self, *args, **options):
        pigments = Pigment.objects.all()
        if not pigments:
            with open(f'{BASE_DIR}/pre_defined_data/pigments.txt', 'r') as f:
                pigments = f.read().split('\n')
                lst = []
                for pigment in pigments:
                    lst.append(Pigment(description=pigment))
            Pigment.objects.bulk_create(lst)
            print('Pigments created')
        else:
            raise CommandError('Pigments already created')
