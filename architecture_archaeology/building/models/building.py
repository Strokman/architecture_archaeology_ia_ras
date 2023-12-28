from django.db import models
from core.models import SlugMixin
from core.models import TimestampMixin
from core.models import DescriptionMixin


class Building(DescriptionMixin, TimestampMixin, SlugMixin):

    name = models.CharField(verbose_name='Название', max_length=255)
    long = models.DecimalField(verbose_name='Долгота', max_digits=23, decimal_places=20)
    lat = models.DecimalField(verbose_name='Широта', max_digits=23, decimal_places=20)
    year_min = models.IntegerField(null=True, blank=True, verbose_name='От')
    year_max = models.IntegerField(null=True, blank=True, verbose_name='До')
    comment = models.TextField(null=True, blank=True)

    site = models.ForeignKey('arch_site.ArchaeologicalSite', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Постройка'
        verbose_name_plural = 'Постройки'
