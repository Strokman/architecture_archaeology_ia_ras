from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Storage


class Command(BaseCommand):
    help = "Создает записи для мест хранения в базе данных"

    def handle(self, *args, **options):
        storages = Storage.objects.all()
        if not storages:
            with open(f'{BASE_DIR}/pre_defined_data/storage.txt', 'r') as f:
                data = f.read().split('\n')
                lst = []
                for row in data:
                    if row:
                        lst.append(Storage(name=row))
            Storage.objects.bulk_create(lst)
            print('Storages created')
        else:
            raise CommandError('Storages already created')
