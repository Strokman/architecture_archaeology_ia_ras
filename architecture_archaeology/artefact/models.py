from django.db import models
from django.urls import reverse_lazy
from core.models import DescriptionMixin
from core.models import TimestampMixin
from core.models import SlugMixin, YearMixin


# Create your models here.
class Artefact(DescriptionMixin, TimestampMixin, SlugMixin, YearMixin):
    """
    Модель описывает таблицу Находок в БД.
    В соотв. с ТЗ заказчика.
    """
    name = models.CharField(verbose_name='Название', null=True, blank=True, max_length=255)
    code = models.IntegerField(null=True, db_index=True, unique=True, verbose_name='Шифр')
    find_date_from = models.IntegerField(null=True, blank=True, verbose_name='Год находки от:')
    find_date_to = models.IntegerField(null=True, blank=True, verbose_name='до:')
    comment = models.TextField(verbose_name='Примечание', null=True, blank=True)
    square_number = models.CharField(max_length=255, verbose_name='Номер квадрата/участка/пласта по археологическим отчетам', null=True, blank=True)
    museum_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='Музейный шифр')

    site = models.ForeignKey('arch_site.ArchaeologicalSite', null=False, verbose_name='Памятник', on_delete=models.CASCADE)
    building = models.ForeignKey("building.Building", verbose_name='Постройка', null=True, blank=True, on_delete=models.CASCADE)
    building_part = models.ForeignKey("building.BuildingPart", verbose_name='Элемент постройки', null=True, blank=True, on_delete=models.CASCADE)

    storage = models.ForeignKey('helpers.Storage', null=False, verbose_name='Место хранения', on_delete=models.CASCADE)

    def get_absolute_url(self):
        if hasattr(self, 'slug'):
            return reverse_lazy(f"{self._meta.app_label}:detail", kwargs={"slug": self.slug})
        return reverse_lazy(f"{self._meta.app_label}:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name if self.name else f'{self._meta.verbose_name} №{self.code}'

    def generate_query_string(self):
        url = f'?code={self.code}'
        return url

    def find_date(self):
        """
        Метод отдает год находки (она может представлять и интервал)
        в формате строки. Если ничего не внесено в БД - пустая строка.
        """
        if not self.find_date_from and not self.find_date_to:
            return ''
        elif not self.find_date_from:
            return f'{self.find_date_to} г.'
        elif not self.find_date_to:
            return f'{self.find_date_from} г.'
        else:
            return f'{self.find_date_from} - {self.find_date_to} гг.'

    class Meta:

        verbose_name = 'Находка'
        verbose_name_plural = 'Находки'
        ordering = ('code', 'id')
