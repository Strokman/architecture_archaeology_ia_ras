from django.core.management.base import BaseCommand, CommandError
from helpers.models import Country


class Command(BaseCommand):
    help = "Создает запись для страны в базе данных"

    def add_arguments(self, parser):
        parser.add_argument("country", nargs="+", type=str)

    def handle(self, *args, **options):
        country_names = options['country']
        print(country_names)
        for name in country_names:
            try:
                Country.objects.create(name=name)
            except Exception as e:
                raise CommandError(f'{e} - error occured')
