from django.db import models
from measurement.models.measurement_base import MeasurementBase


class ScanningElectronMicroscopy(MeasurementBase):

    elements = models.ManyToManyField('helpers.Element', blank=True, verbose_name='Элементы периодической таблицы')

    class Meta:
        verbose_name = verbose_name_plural = 'Растровая электронная микроскопия'
        ordering = ('created_at', 'id')
