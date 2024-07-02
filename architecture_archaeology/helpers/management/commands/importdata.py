from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Storage
from building.models import Building
from arch_site.models import ArchaeologicalSite
from artwork.models import Frescoe
from csv import DictReader


class Command(BaseCommand):
    help = "Импорт данных в базу"

    def handle(self, *args, **options):
        with open(f'{BASE_DIR}/pre_defined_data/frescoes_main.csv', 'r', encoding='utf-8-sig') as f:
            data = DictReader(f, delimiter=';')
            model_data = dict()
            for row in data:
                
                if row['№']:
                    # print(row)
                    storage = Storage.objects.get(name=row['Место хранения'])
                    model_data['storage'] = storage
                    try:
                        site = ArchaeologicalSite.objects.get(name=row['Памятник'].replace('«', '').replace('»', ''))
                    except:
                        print(row['Памятник'])
                    try:
                        building = Building.objects.get(name=row['Постройка'].strip())
                    except:
                        print(row['Постройка'])
                        print(row)
                    match row['Вид']:
                        case 'Индивидуальная фреска':
                            model_data['kind'] = Frescoe.Kind.INDIVIDUAL
                        case 'Лоток':
                            model_data['kind'] = Frescoe.Kind.LOTOK
                    match row['Тип']:
                        case 'масс.':
                            model_data['type'] = Frescoe.Type.MASS
                        case 'инд.':
                            model_data['type'] = Frescoe.Type.INDIVIDUAL
                    model_data['comment'] = row['Примечание']
                    model_data['museum_code'] = row['Индивид. номер \n(музейный, если есть)']
                    model_data['square_number'] = row['Номер квадрата/участка\n по археологическим отчётам']
                    # print(model_data)
