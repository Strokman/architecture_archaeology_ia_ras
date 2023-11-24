from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Color


class Command(BaseCommand):
    help = "Создает записи для материалов в базе данных"

    def handle(self, *args, **options):
        colors = Color.objects.all()
        if not colors:
            with open(f'{BASE_DIR}/pre_defined_data/colors.txt', 'r') as f:
                data = f.read().split('\n')
                lst = []
                for row in data:
                    clean_data = row.replace('(', '').replace(')', '').split()
                    color = clean_data[0]
                    code = clean_data[1]
                    lst.append(Color(description=color, code=code))
            Color.objects.bulk_create(lst)
            print('Colors created')
        else:
            raise CommandError('Colors already created')
