from django.core.management.base import BaseCommand, CommandError
from file.models import FileType


class Command(BaseCommand):
    help = "Создает записи для типов файлов"

    def handle(self, *args, **options):
        colors = FileType.objects.all()
        if not colors:
            filetypes = ['фотография', 'план', 'отчет']
            lst = []
            for type in filetypes:
                lst.append(FileType(name=type))
            FileType.objects.bulk_create(lst)
            print('FileTypes created')
        else:
            raise CommandError('FileTypes already created')
