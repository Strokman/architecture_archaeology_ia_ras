from django.db import models
from core.timestamp_model import TimestampModel
from core.description_model import DescriptionModel


# Create your models here.
class Artwork(DescriptionModel):
    code = models.CharField(max_length=100)

    preservation_id = models.ForeignKey('artwork.Preservation', on_delete=models.CASCADE)


class Preservation(DescriptionModel):
    pass

