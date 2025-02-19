from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import DescriptionMixin
from core.models import TimestampMixin
from core.models import SlugMixin
from artwork.models.artwork_base import ArtworkBase


# Create your models here.
class Frescoe(ArtworkBase, DescriptionMixin, TimestampMixin, SlugMixin):
    class Type(models.TextChoices):
        """
        В соотв. с ТЗ фрески могут быть массовыми и индивидуальными
        """
        MASS = 'M', _('массовый')
        INDIVIDUAL = 'I', _('индивидуальный')

    class Kind(models.TextChoices):
        """
        Фреска может быть индивидуальной и в виде лотка.
        Поэтому сделано поле для выбора. Не отдельная модель,
        так как разницы, кроме этого - никакой нет
        """
        LOTOK = 'L', _('лоток')
        INDIVIDUAL = 'I', _('индивидуальная фреска')

    type = models.CharField(
        verbose_name='Тип',
        null=False,
        max_length=100,
        choices=Type
        )
    kind = models.CharField(
        verbose_name='Вид',
        default=Kind.INDIVIDUAL,
        max_length=255,
        choices=Kind
        )
    size = models.CharField(
        verbose_name='Размер',
        null=True,
        blank=True,
        max_length=255
        )
    amount = models.IntegerField(
        verbose_name='Количество фрагментов',
        null=True,
        blank=True
        )
    museum_code = models.CharField(
        verbose_name='Музейный шифр',
        null=True,
        blank=True,
        max_length=255
        )
    square_number = models.CharField(
        max_length=255,
        verbose_name='Номер квадрата/участка/пласта по \
                      археологическим отчетам',
        null=True,
        blank=True
        )

    storage = models.ForeignKey(
        'helpers.Storage',
        null=False,
        verbose_name='Место хранения',
        on_delete=models.PROTECT
        )
    indoor_artwork = models.ForeignKey(
        'artwork.IndoorArtwork',
        null=True, blank=True,
        verbose_name='Изображение в постройке',
        on_delete=models.PROTECT
        )

    def __str__(self):
        return f'{self.name}, фреска №{self.code}' if self.name \
            else f'{self.get_kind_display().capitalize()} №{self.code}'

    class Meta:
        verbose_name = 'Индивидуальная фреска'
        verbose_name_plural = 'Индивидуальные фрески'
        ordering = ('code', 'id')
