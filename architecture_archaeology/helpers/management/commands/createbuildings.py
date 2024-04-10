from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Element
from building.models import Building
from csv import DictReader


class Command(BaseCommand):
    help = "Создает записи для элементов периодической таблицы в базе данных"

    def handle(self, *args, **options):
        with open(f'{BASE_DIR}/pre_defined_data/buildings.csv', 'r', encoding='utf-8') as f:
            # elements = []
            row = DictReader(f, delimiter=',')
            for column in row:
                print(column)
        #         element = Element(atomic_number=column['AtomicNumber'], name=column['Element'], symbol=column['Symbol'])
        #         elements.append(element)
        # Element.objects.bulk_create(elements)
        print('Successfully created')
        # else:
            # raise CommandError('Elements already created')