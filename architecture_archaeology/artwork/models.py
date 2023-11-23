from django.db import models
from core.description_mixin import DescriptionMixin
from core.timestamp_mixin import TimestampMixin


# Create your models here.
class Artwork(DescriptionMixin, TimestampMixin):
    code = models.CharField(max_length=100)

    preservation_id = models.ForeignKey('helpers.Preservation', on_delete=models.CASCADE)
