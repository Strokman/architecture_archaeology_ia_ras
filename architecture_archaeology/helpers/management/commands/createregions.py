from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Region, Country
from csv import DictReader


class Command(BaseCommand):
    help = "Создает записи для регионов в базе данных"

    def add_arguments(self, parser):
        parser.add_argument("country", nargs="+", type=str)

    def handle(self, *args, **options):
        regions_from_db = Region.objects.all()
        if not regions_from_db:

            country_arg = options['country']
            try:
                country: Country = Country.objects.get(name=country_arg[0])
                regions = []
                with open(f'{BASE_DIR}/pre_defined_data/regions.csv', 'r') as f:
                    row = DictReader(f, delimiter=',')
                    for column in row:
                        region = Region(name=column['name_with_type'], country=country)
                        regions.append(region)
                Region.objects.bulk_create(regions)
                print('Successfully created')
            except Country.DoesNotExist:
                raise CommandError(f'{country_arg} does not exist')
        else:
            raise CommandError('Regions already created')
