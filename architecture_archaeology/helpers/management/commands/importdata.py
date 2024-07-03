from django.core.management.base import BaseCommand, CommandError
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Storage, Color
from building.models import Building
from arch_site.models import ArchaeologicalSite
from artwork.models import Frescoe
from csv import DictReader
from core.services.index_service import sequence_id


class Command(BaseCommand):
    help = "Импорт данных в базу"

    def handle(self, *args, **options):
        with open(f'{BASE_DIR}/pre_defined_data/frescoes_main.csv', 'r', encoding='utf-8-sig') as f:
            data = DictReader(f, delimiter=';')
            
            for row in data:
                
                if row['№']:
                    
                    model_data = dict()
                    storage = Storage.objects.get(name=row['Место хранения'])
                    model_data['storage'] = storage
                    try:
                        site = ArchaeologicalSite.objects.get(name=row['Памятник'].strip())
                        model_data['site'] = site
                    except:
                        print(row['Памятник'])
                        pass
                    try:
                        building = Building.objects.get(name=row['Постройка'].strip(), site_id=site.id)
                        model_data['building'] = building
                    except:
                        print(row['Постройка'])
                        pass
                    match row['Вид']:
                        case 'Индивидуальная фреска':
                            model_data['kind'] = Frescoe.Kind.INDIVIDUAL
                        case 'Лоток':
                            model_data['kind'] = Frescoe.Kind.LOTOK
                    match row['Тип']:
                        case 'Массовый':
                            model_data['type'] = Frescoe.Type.MASS
                        case 'Индивидуальный':
                            model_data['type'] = Frescoe.Type.INDIVIDUAL
                    if building:
                        model_data['building'] = building

                    find_date = row['Год\nнаходки']
                    if find_date:
                        if '-' in find_date:
                            date = find_date.split('-')
                            find_date_from = date[0]
                            find_date_to = date[1]
                            model_data['find_date_from'] = find_date_from
                            model_data['find_date_to'] = find_date_to
                        else:
                            find_date_from = find_date

                            model_data['find_date_from'] = find_date_from
                    model_data['name'] = row['Название']
                    amount = row['Количество \nфрагментов']
                    if amount and amount.isdigit():
                        model_data['amount'] = amount
                    
                    model_data['comment'] = row['Примечание']
                    if row['цвет']:
                        model_data['comment'] += f'. Исправить цвета, исходные данные: {row['цвет']}'
                    model_data['museum_code'] = row['Индивид. номер \n(музейный, если есть)']
                    model_data['square_number'] = row['Номер квадрата/участка\n по археологическим отчётам']
                    model_data['code'] = sequence_id()
                    if site.name == 'Эталон':
                        model_data['name'] = 'Эталон' + str(model_data['code'])
                    if site.name == 'Занято':
                        model_data['name'] = 'Резерв' + str(model_data['code'])
                    model_data['creator_id'] = model_data['editor_id'] = 1
                    frescoe = Frescoe.objects.create(**model_data)
                    # if color:
                    #     frescoe.color.add(color)
                    #     frescoe.save()
