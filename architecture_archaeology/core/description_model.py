from django.db import models
from core.timestamp_model import TimestampModel


class DescriptionModel(TimestampModel):

    description = models.CharField(max_length=100, verbose_name='Описание')

    class Meta:

        abstract = True