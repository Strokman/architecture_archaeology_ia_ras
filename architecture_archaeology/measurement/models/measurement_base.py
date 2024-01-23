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

    name = models.CharField(verbose_name='Название', max_length=255)
    measurement_date = models.DateField(verbose_name='Дата исследования', null=False)

    material = models.CharField(max_length=100, choices=Material)
    operator = models.CharField(verbose_name='Оператор', max_length=255, null=False)
    equipment = models.CharField(verbose_name='Оборудование', max_length=255, null=False)
    conditions = models.CharField(verbose_name='Условия', max_length=255, null=False)

    color = models.ManyToManyField('helpers.Color', verbose_name='Цвета')

    comment = models.TextField(verbose_name='Примечание', null=True)
    pigment = models.ManyToManyField('helpers.Pigment', verbose_name='Пигменты')

    additional_elements = models.CharField(verbose_name='Дополнительные выявленные соединения', max_length=255)
    source = models.CharField(verbose_name='Источник референсных значений', max_length=255)
    

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
