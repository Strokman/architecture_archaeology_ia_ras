from core.models import DescriptionMixin
from core.models import TimestampMixin
from core.models import SlugMixin
from artwork.models.artwork_base import ArtworkBase


# Create your models here.
class IndoorArtwork(ArtworkBase, DescriptionMixin, TimestampMixin, SlugMixin):

    def __str__(self):
        return self.name if self.name else f'{self._meta.verbose_name} №{self.code}'

    class Meta:

        verbose_name = 'Изображение в постройке'
        verbose_name_plural = 'Изображения в постройке'
