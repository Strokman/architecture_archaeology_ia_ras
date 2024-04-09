from django.db import models
from measurement.models.measurement_base import MeasurementBase


class ScanningElectronMicroscopy(MeasurementBase):

    elements = models.CharField(verbose_name='Элементы', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Растровая электронная микроскопия'
        ordering = ('created_at', 'id')
