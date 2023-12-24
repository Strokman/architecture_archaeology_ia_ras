from django.core.management.base import BaseCommand, CommandError
from helpers.models import Preservation


class Command(BaseCommand):
    help = "Создает записи для сохранности в базе данных"
    preservations = ['In situ', 'Археологическая фреска']

    def handle(self, *args, **options):
        preserv = Preservation.objects.all()
        if not preserv:
            lst = []
            for pres in self.preservations:
                lst.append(Preservation(description=pres))
            Preservation.objects.bulk_create(lst)
            print('Preservations created')
        else:
            raise CommandError('Preservations already created')