from django.db import models
from django.utils.translation import gettext_lazy as _
from measurement.models.measurement_base import MeasurementBase


class InfraredRamanMicroscopy(MeasurementBase):
    class Method(models.TextChoices):
        INFRARED = 'IR', _('ИК спектроскопия')
        RAMAN_SPECTR = 'RS', _('рамановская спектроскопия')

    method = models.CharField(verbose_name='Метод', choices=Method, max_length=255, null=True)
    groups = models.CharField(verbose_name='Функциональные группы и соединения', max_length=255, null=True)

    class Meta:
        verbose_name = verbose_name_plural = 'ИК и рамановская спектроскопия'
