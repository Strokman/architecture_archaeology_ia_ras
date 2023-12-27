from django.db import models
from core.models import DescriptionMixin
from core.models import TimestampMixin
from core.models import SlugMixin


# Create your models here.
class Lotok(DescriptionMixin, TimestampMixin, SlugMixin):
    size = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    museum_code = models.CharField(max_length=255)

    storage = models.ForeignKey('helpers.Storage', on_delete=models.PROTECT)
    indoor_artwork = models.ForeignKey('artwork.IndoorArtwork', on_delete=models.PROTECT)