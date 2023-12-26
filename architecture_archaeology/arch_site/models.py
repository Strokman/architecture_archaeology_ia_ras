from django.db import models

from core import TimestampMixin
from core import DescriptionMixin
from core import SlugMixin


class ArchaeologicalSite(DescriptionMixin, TimestampMixin, SlugMixin):

    name = models.CharField(verbose_name='Название', max_length=255)
    long = models.DecimalField(verbose_name='Долгота', max_digits=23, decimal_places=20, help_text='Координаты в формате DD.DDDD')
    lat = models.DecimalField(verbose_name='Широта', max_digits=23, decimal_places=20, help_text='Координаты в формате DD.DDDD')
    year_min = models.IntegerField(verbose_name='Датировка от:', null=False)
    year_max = models.IntegerField(verbose_name='до:', null=False)
    comment = models.TextField(verbose_name='Примечание', null=True)

    region = models.ForeignKey('helpers.Region', verbose_name='Административная принадлежность', null=False, on_delete=models.PROTECT, related_name='sites')

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Археологический памятник'
        verbose_name_plural = 'Археологические памятники'
