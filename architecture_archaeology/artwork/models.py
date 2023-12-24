from django.db import models
from core.description_mixin import DescriptionMixin
from core.timestamp_mixin import TimestampMixin


# Create your models here.
class Artwork(DescriptionMixin, TimestampMixin):
    code = models.CharField(max_length=100)
    size = models.CharField(max_length=255)
    year_min = models.IntegerField(null=False, verbose_name='От')
    year_max = models.IntegerField(null=False, verbose_name='До')

    building = models.ForeignKey('building.Building', on_delete=models.PROTECT)
    building_part = models.ForeignKey('building.BuildingPart', on_delete=models.PROTECT)
    color = models.ManyToManyField('helpers.Color')
    preservation = models.ForeignKey('helpers.Preservation', on_delete=models.PROTECT)
