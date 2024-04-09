from django.db import models
from django.urls import reverse_lazy
from core.models import DescriptionMixin
from core.models import TimestampMixin
from core.models import SlugMixin, YearMixin


# Create your models here.
class Artefact(DescriptionMixin, TimestampMixin, SlugMixin, YearMixin):
    name = models.CharField(verbose_name='Название', null=True, blank=True, max_length=255)
    code = models.IntegerField(null=True, db_index=True, unique=True, verbose_name='Шифр')
    find_date_from = models.IntegerField(null=True, blank=True, verbose_name='Год находки от:')
    find_date_to = models.IntegerField(null=True, blank=True, verbose_name='до:')
    comment = models.TextField(verbose_name='Примечание', null=True, blank=True)
    square_number = models.CharField(max_length=255, verbose_name='Номер квадрата/участка/пласта по археологическим отчетам', null=True, blank=True)
    museum_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='Музейный шифр')

    site = models.ForeignKey('arch_site.ArchaeologicalSite', null=False, verbose_name='Памятник', on_delete=models.PROTECT)
    storage = models.ForeignKey('helpers.Storage', null=False, verbose_name='Место хранения', on_delete=models.PROTECT)

    def get_absolute_url(self):
        if hasattr(self, 'slug'):
            return reverse_lazy(f"{self._meta.app_label}:detail", kwargs={"slug": self.slug})
        return reverse_lazy(f"{self._meta.app_label}:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name if self.name else f'{self._meta.verbose_name} №{self.code}'

    def generate_query_string(self):
        url = f'{reverse_lazy("measurement:submit-rfa")}?code={self.code}&obj={self.__class__.__name__.lower()}'
        return url

    class Meta:

        verbose_name = 'Находка'
        verbose_name_plural = 'Находки'
        ordering = ('code', 'id')
