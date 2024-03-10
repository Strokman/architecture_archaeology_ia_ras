from django.db import models

from django.utils.translation import gettext_lazy as _
from core.models import TimestampMixin
from core.models import DescriptionMixin
from core.models import SlugMixin, YearMixin


class ArchaeologicalSite(DescriptionMixin, TimestampMixin, SlugMixin, YearMixin):
    class Preservation(models.TextChoices):
        PRESERVED = 'P', _('сохранился')
        DESTROYED = 'D', _('не сохранился')

    name = models.CharField(verbose_name='Название', max_length=255, help_text='Название памятника', db_index=True)
    long = models.DecimalField(verbose_name='Долгота', max_digits=23, decimal_places=20, help_text='Координаты в формате DD.DDDD')
    lat = models.DecimalField(verbose_name='Широта', max_digits=23, decimal_places=20, help_text='Координаты в формате DD.DDDD')
    preservation = models.CharField(verbose_name='Сохранность', null=False, max_length=100, choices=Preservation)
    comment = models.TextField(verbose_name='Примечание', null=True, blank=True)
  
    region = models.ForeignKey('helpers.Region',
                               verbose_name='Административная принадлежность',
                               null=False,
                               on_delete=models.PROTECT,
                               related_name='sites',
                               help_text='Выберите один из регионов')

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Памятник'
        verbose_name_plural = 'Памятники'
        ordering = ('name',)
