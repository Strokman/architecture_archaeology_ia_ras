from django.db import models
from core.models import SlugMixin
from core.models import TimestampMixin
from core.models import DescriptionMixin, YearMixin


class Building(DescriptionMixin, TimestampMixin, SlugMixin, YearMixin):

    name = models.CharField(verbose_name='Название', max_length=255)
    long = models.DecimalField(verbose_name='Долгота', max_digits=23, decimal_places=20)
    lat = models.DecimalField(verbose_name='Широта', max_digits=23, decimal_places=20)
    comment = models.TextField(verbose_name='Примечание', null=True, blank=True)

    site = models.ForeignKey('arch_site.ArchaeologicalSite', verbose_name='Памятник', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Постройка'
        verbose_name_plural = 'Постройки'
