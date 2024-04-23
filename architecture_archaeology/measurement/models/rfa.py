from django.db import models
from measurement.models.measurement_base import MeasurementBase


class RFA(MeasurementBase):

    element = models.ManyToManyField('helpers.Element', blank=True, verbose_name='Элементы периодической таблицы')

    class Meta:
        verbose_name = verbose_name_plural = 'РФА'
        ordering = ('created_at', 'id')

