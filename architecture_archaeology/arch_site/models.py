from django.db import models
# from core.utils import slugify
from django.urls import reverse_lazy
from core import TimestampMixin
from core import DescriptionMixin
from core import SlugMixin


class ArchaeologicalSite(DescriptionMixin, TimestampMixin, SlugMixin):

    name = models.CharField(verbose_name='Название', max_length=255)
    long = models.DecimalField(verbose_name='Долгота', max_digits=23, decimal_places=20, help_text='Координаты в формате DD.DDDD')
    lat = models.DecimalField(verbose_name='Широта', max_digits=23, decimal_places=20, help_text='Координаты в формате DD.DDDD')
    year_min = models.IntegerField(verbose_name='Датировка от:', null=False)
    year_max = models.IntegerField(verbose_name='до:', null=False)
    comment = models.TextField(verbose_name='Примечание', null=True)

    region = models.ForeignKey('helpers.Region', verbose_name='Административная принадлежность', null=False, on_delete=models.PROTECT, related_name='sites')
    # file = models.ManyToManyField('file.File', related_name='sites')

    def get_absolute_url(self):
        return reverse_lazy("arch_site", kwargs={"pk": self.pk})

    def get_url(self):
        return self.slug

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Археологический памятник'
        verbose_name_plural = 'Археологические памятники'