from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import SlugMixin
from core.models import TimestampMixin
from core.models import DescriptionMixin, YearMixin


class Building(DescriptionMixin, TimestampMixin, SlugMixin, YearMixin):
    class Preservation(models.TextChoices):
        PRESERVED = 'P', _('сохранился')
        DESTROYED = 'D', _('не сохранился')

    name = models.CharField(verbose_name='Название', max_length=255)
    long = models.DecimalField(verbose_name='Долгота', max_digits=23, decimal_places=20)
    lat = models.DecimalField(verbose_name='Широта', max_digits=23, decimal_places=20)
    preservation = models.CharField(verbose_name='Сохранность', null=False, max_length=100, choices=Preservation)
    comment = models.TextField(verbose_name='Примечание', null=True, blank=True)

    site = models.ForeignKey('arch_site.ArchaeologicalSite', verbose_name='Памятник', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Постройка'
        verbose_name_plural = 'Постройки'
        ordering = ('name', 'id')
