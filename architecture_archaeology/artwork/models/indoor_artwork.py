from django.db import models
from core.description_mixin import DescriptionMixin
from core.timestamp_mixin import TimestampMixin
from core.slug_mixin import SlugMixin
from core.models import ArtworkBase


# Create your models here.
class IndoorArtwork(ArtworkBase, DescriptionMixin, TimestampMixin, SlugMixin):
    pass