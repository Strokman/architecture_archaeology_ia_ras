from django.db import models
from measurement.models.measurement_base import MeasurementBase


class ScanningElectronMicroscopy(MeasurementBase):

    elements = models.CharField(verbose_name='Элементы', max_length=255, null=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Растровая электронная микроскопия'
