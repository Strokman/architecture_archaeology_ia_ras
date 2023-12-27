from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import DescriptionMixin
from core.models import TimestampMixin
from core.models import SlugMixin
from artwork.models.artwork_base import ArtworkBase


# Create your models here.
class Frescoe(ArtworkBase, DescriptionMixin, TimestampMixin, SlugMixin):
    class Type(models.TextChoices):
        MASS = 'M', _('массовый')
        INDIVIDUAL = 'I', _('индивидуальный')

    type = models.CharField(max_length=100, choices=Type)
    size = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    museum_code = models.CharField(max_length=255)

    storage = models.ForeignKey('helpers.Storage', on_delete=models.PROTECT)
    indoor_artwork = models.ForeignKey('artwork.IndoorArtwork', on_delete=models.PROTECT)
