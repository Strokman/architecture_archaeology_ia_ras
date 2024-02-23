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

    type = models.CharField(verbose_name='Тип', max_length=100, choices=Type)
    size = models.CharField(verbose_name='Размер', max_length=255)
    amount = models.IntegerField(verbose_name='Количество фрагментов', null=True)
    museum_code = models.CharField(verbose_name='Музейный шифр', max_length=255)

    storage = models.ForeignKey('helpers.Storage', verbose_name='Место хранения', on_delete=models.PROTECT)
    indoor_artwork = models.ForeignKey('artwork.IndoorArtwork', verbose_name='Изображение в постройке', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Индивидуальная фреска'
        verbose_name_plural = 'Индивидуальные фрески'
