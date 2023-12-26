from django.db import models
from core.description_mixin import DescriptionMixin
from core.timestamp_mixin import TimestampMixin
from core.slug_mixin import SlugMixin


# Create your models here.
class Lotok(DescriptionMixin, TimestampMixin, SlugMixin):
    size = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    museum_code = models.CharField(max_length=255)

    storage = models.ForeignKey('helpers.Storage', on_delete=models.PROTECT)
    indoor_artwork = models.ForeignKey('artwork.IndoorArtwork', on_delete=models.PROTECT)