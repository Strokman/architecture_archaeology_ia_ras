from django.db import models
from core.utils import slugify
from core.timestamp_mixin import TimestampMixin
from core.description_mixin import DescriptionMixin


class Building(DescriptionMixin, TimestampMixin):

    name = models.CharField(verbose_name='Название', max_length=255)
    long = models.DecimalField(verbose_name='Долгота', max_digits=23, decimal_places=20)
    lat = models.DecimalField(verbose_name='Широта', max_digits=23, decimal_places=20)
    slug = models.SlugField(default='', null=False, db_index=True)

    region = models.ForeignKey('helpers.Region', null=False, on_delete=models.PROTECT, related_name='buildings')
    # date = models.ForeignKey('helpers.Date', null=True, on_delete=models.SET_NULL)
    # comment = models.ForeignKey('helpers.Comment', null=True, on_delete=models.SET_NULL, related_name='buildings')

    file = models.ManyToManyField('helpers.File')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Building, self).save(*args, **kwargs)

    def get_url(self):
        return self.slug

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Постройка'
        verbose_name_plural = 'Постройки'
