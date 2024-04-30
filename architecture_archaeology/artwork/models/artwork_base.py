from django.db import models
from django.urls import reverse_lazy
from core.models import DescriptionMixin
from core.models import TimestampMixin
from core.models import SlugMixin, YearMixin


class ArtworkBase(DescriptionMixin, TimestampMixin, SlugMixin, YearMixin):
    name = models.CharField(
        verbose_name='Название',
        null=True,
        blank=True,
        max_length=255
        )
    code = models.IntegerField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='Шифр'
        )
    find_date_from = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Год находки от:'
        )
    find_date_to = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='до:'
        )
    comment = models.TextField(
        verbose_name='Примечание',
        null=True,
        blank=True)

    site = models.ForeignKey(
        "arch_site.ArchaeologicalSite",
        verbose_name='Памятник',
        null=False,
        on_delete=models.CASCADE
        )
    building = models.ForeignKey(
        "building.Building",
        verbose_name='Постройка',
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    building_part = models.ForeignKey(
        "building.BuildingPart",
        verbose_name='Элемент постройки',
        null=True,
        blank=True,
        on_delete=models.PROTECT
        )
    color = models.ManyToManyField(
        'helpers.Color',
        blank=True,
        verbose_name='Цвета'
        )
    preservation = models.ForeignKey(
        'helpers.Preservation',
        null=True,
        blank=True,
        verbose_name='Сохранность',
        on_delete=models.PROTECT
        )

    def get_absolute_url(self):
        if hasattr(self, 'slug'):
            return reverse_lazy(
                f"{self._meta.app_label}:detail-{self.__class__.
                                                 __name__.lower()}",
                kwargs={"slug": self.slug}
                )
        return reverse_lazy(
            f"{self._meta.app_label}:detail-{self.__class__.
                                             __name__.lower()}",
            kwargs={"pk": self.pk})

    def generate_query_string(self):
        url = f'?code={self.code}'
        return url

    def find_date(self):
        if not self.find_date_from and not self.find_date_to:
            return ''
        return f'{self.find_date_from} - {self.find_date_to} гг.' \
            if self.find_date_to else f'{self.find_date_from} г.'

    class Meta:
        abstract = True
