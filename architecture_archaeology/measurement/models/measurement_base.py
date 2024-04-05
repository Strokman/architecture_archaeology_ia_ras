from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimestampMixin
from core.models import SlugMixin


# Create your models here.
class MeasurementBase(TimestampMixin, SlugMixin):

    class Material(models.TextChoices):
        COLOR_LAYER = 'CL', _('красочный слой')
        PLASTER = 'P', _('штукатурка')
        CEMENT = 'C', _('раствор')

    name = models.CharField(verbose_name='Название', null=True, blank=True, max_length=255)
    measurement_date = models.DateField(verbose_name='Дата исследования', null=False)

    material = models.CharField(verbose_name='Тип вещества', null=False, max_length=100, choices=Material)
    operator = models.CharField(verbose_name='Оператор', max_length=255, null=False)
    equipment = models.CharField(verbose_name='Оборудование', max_length=255, null=False)
    conditions = models.CharField(verbose_name='Условия', max_length=255, null=False)

    color = models.ManyToManyField('helpers.Color', blank=True, verbose_name='Цвета')

    comment = models.TextField(verbose_name='Примечание', null=True, blank=True, max_length=2000)
    pigment = models.ManyToManyField('helpers.Pigment', blank=True, verbose_name='Пигменты')

    additional_elements = models.CharField(verbose_name='Дополнительные выявленные соединения', null=True, blank=True, max_length=1000)
    source = models.CharField(verbose_name='Источник референсных значений', null=True, blank=True, max_length=5000)

    def __str__(self):
        return self.name if self.name else f'{self._meta.verbose_name} №{self.id}'

    class Meta:
        abstract = True
