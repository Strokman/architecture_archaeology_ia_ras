from django.db import models
from core.utils import slugify
from django.urls import reverse_lazy
from core.timestamp_mixin import TimestampMixin
from core.description_mixin import DescriptionMixin


class ArchaeologicalSite(DescriptionMixin, TimestampMixin):

    name = models.CharField(verbose_name='Название', max_length=255)
    long = models.DecimalField(verbose_name='Долгота', max_digits=23, decimal_places=20)
    lat = models.DecimalField(verbose_name='Широта', max_digits=23, decimal_places=20)
    slug = models.SlugField(default='', null=False, db_index=True)
    year_min = models.IntegerField(null=False)
    year_max = models.IntegerField(null=False)

    region = models.ForeignKey('helpers.Region', null=False, on_delete=models.PROTECT, related_name='sites')
    # comment = models.ForeignKey('helpers.Comment', null=True, on_delete=models.SET_NULL, related_name='sites')

    # file = models.ManyToManyField('file.File', related_name='sites')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ArchaeologicalSite, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("arch_site", kwargs={"pk": self.pk})

    def get_url(self):
        return self.slug

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Археологический памятник'
        verbose_name_plural = 'Археологические памятники'