from django.db import models
from core.timestamp_model import TimestampModel
from core.description_model import DescriptionModel


# Create your models here.
class Building(DescriptionModel):
    name = models.CharField(max_length=255)
    long = models.DecimalField(max_digits=23, decimal_places=20)
    lat = models.DecimalField(max_digits=23, decimal_places=20)

    def __str__(self):
        return f'{self.name}'