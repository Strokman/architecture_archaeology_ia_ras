from django.db import models
from django.urls import reverse_lazy
from core.models import DescriptionMixin
from core.models import TimestampMixin
from core.models import SlugMixin, YearMixin


class ArtworkBase(DescriptionMixin, TimestampMixin, SlugMixin, YearMixin):
    name = models.CharField(verbose_name='Название', max_length=255)
    code = models.CharField(verbose_name='Шифр', max_length=100)
    find_date_from = models.IntegerField(null=True, verbose_name='Год находки от:')
    find_date_to = models.IntegerField(null=True, verbose_name='до:')
    comment = models.TextField(verbose_name='Примечание', null=True)
    square_number = models.CharField(max_length=255, verbose_name='Номер квадрата/участка/пласта по археологическим отчетам', null=True)

    site = models.ForeignKey("arch_site.ArchaeologicalSite", verbose_name='Памятник', null=False, on_delete=models.CASCADE)

    color = models.ManyToManyField('helpers.Color', verbose_name='Цвета')
    preservation = models.ForeignKey('helpers.Preservation', verbose_name='Сохранность', on_delete=models.PROTECT)

    def get_absolute_url(self):
        if hasattr(self, 'slug'):
            return reverse_lazy(f"{self._meta.app_label}:detail-{self.__class__.__name__.lower()}", kwargs={"slug": self.slug})
        return reverse_lazy(f"{self._meta.app_label}:detail-{self.__class__.__name__.lower()}", kwargs={"pk": self.pk})

    class Meta:
        abstract = True
