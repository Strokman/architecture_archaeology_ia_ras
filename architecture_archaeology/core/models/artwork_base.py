from django.db import models
from core.description_mixin import DescriptionMixin
from core.timestamp_mixin import TimestampMixin
from core.slug_mixin import SlugMixin


# Create your models here.
class ArtworkBase(DescriptionMixin, TimestampMixin, SlugMixin):
    name = models.CharField(verbose_name='Название', max_length=255)
    code = models.CharField(verbose_name='Шифр', max_length=100)
    year_min = models.IntegerField(null=False, verbose_name='Датировка от:')
    year_max = models.IntegerField(null=False, verbose_name='до:')
    find_date_from = models.IntegerField(null=True, verbose_name='Год находки от:')
    find_date_to = models.IntegerField(null=True, verbose_name='до:')
    comment = models.TextField(verbose_name='Примечание', null=True)
    square_number = models.IntegerField(verbose_name='Номер квадрата/участка/пласта по археологическим отчетам', null=True)

    building = models.ForeignKey('building.Building', verbose_name='Постройка', on_delete=models.PROTECT)
    building_part = models.ForeignKey('building.BuildingPart', verbose_name='Элемент постройки', on_delete=models.PROTECT)
    color = models.ManyToManyField('helpers.Color', verbose_name='Цвета')
    preservation = models.ForeignKey('helpers.Preservation', verbose_name='Сохранность', on_delete=models.PROTECT)

    class Meta:
        abstract = True
