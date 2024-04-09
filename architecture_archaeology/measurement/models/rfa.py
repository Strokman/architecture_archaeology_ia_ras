from django.db import models
from measurement.models.measurement_base import MeasurementBase


class RFA(MeasurementBase):

    # TODO: сделать множественный выбор из таблицы менделеева
    elements = models.CharField(verbose_name='Элементы', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'РФА'
        ordering = ('created_at', 'id')

