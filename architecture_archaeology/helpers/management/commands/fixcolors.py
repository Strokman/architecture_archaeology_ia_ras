from django.core.management.base import BaseCommand
from architecture_archaeology.settings import BASE_DIR
from helpers.models import Color
from artwork.models import Frescoe
from csv import DictReader



class Command(BaseCommand):
    help = "Привязка цветов из файла"

    def handle(self, *args, **options):
        with open(f'{BASE_DIR}/pre_defined_data/frescoes_main.csv', 'r', encoding='utf-8-sig') as f:
            data = DictReader(f, delimiter=';')
            
            for row in data:
                if row['№']:
                    try:
                        color = row['цвет'].split()
                        frescoe = Frescoe.objects.get(code=row['№'])
                        frescoe.color.clear()
                        if color:
                            for i in color:
                                try:
                                    db_color = Color.objects.get(description=i.lower())
                                    frescoe.color.add(db_color)
                                    frescoe.save()
                                except:
                                    print(i)

                    except KeyError:
                        pass
