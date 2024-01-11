from django.db import models
from measurement.models.measurement_base import MeasurementBase


class Roentgen(MeasurementBase):

    mineral = models.ManyToManyField('helpers.Mineral', verbose_name='Минералы')

    class Meta:
        verbose_name = 'Рентгенофазовый и рентгеноструктурный анализ'
        verbose_name_plural = 'Рентгенофазовый и рентгеноструктурный анализы'