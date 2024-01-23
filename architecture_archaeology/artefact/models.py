from django.db import models
from django.urls import reverse_lazy
from core.models import DescriptionMixin
from core.models import TimestampMixin
from core.models import SlugMixin


# Create your models here.
class Artefact(DescriptionMixin, TimestampMixin, SlugMixin):
    name = models.CharField(verbose_name='Название', max_length=255)
    code = models.CharField(verbose_name='Шифр', max_length=100)
    year_min = models.IntegerField(null=False, verbose_name='Датировка от:')
    year_max = models.IntegerField(null=False, verbose_name='до:')
    find_date_from = models.IntegerField(null=True, verbose_name='Год находки от:')
    find_date_to = models.IntegerField(null=True, verbose_name='до:')
    comment = models.TextField(verbose_name='Примечание', null=True)
    square_number = models.CharField(max_length=255, verbose_name='Номер квадрата/участка/пласта по археологическим отчетам', null=True)
    museum_code = models.CharField(max_length=255, verbose_name='Музейный шифр')

    site = models.ForeignKey('arch_site.ArchaeologicalSite', verbose_name='Постройка', on_delete=models.PROTECT)
    storage = models.ForeignKey('helpers.Storage', verbose_name='Место хранения', on_delete=models.PROTECT)

    def get_absolute_url(self):
        if hasattr(self, 'slug'):
            return reverse_lazy(f"{self._meta.app_label}:detail", kwargs={"slug": self.slug})
        return reverse_lazy(f"{self._meta.app_label}:detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Находка'
        verbose_name_plural = 'Находки'
