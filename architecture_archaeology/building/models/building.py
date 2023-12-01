from django.db import models
from django.utils.text import slugify
from core.timestamp_mixin import TimestampMixin
from core.description_mixin import DescriptionMixin


class Building(DescriptionMixin, TimestampMixin):

    name = models.CharField(verbose_name='Название', max_length=255)
    long = models.DecimalField(verbose_name='Долгота', max_digits=23, decimal_places=20)
    lat = models.DecimalField(verbose_name='Широта', max_digits=23, decimal_places=20)
    slug = models.SlugField(default='', null=False, db_index=True)

    region = models.ForeignKey('helpers.Region', null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Building, self).save(*args, **kwargs)

    def get_url(self):
        return slugify(self.name)

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Постройка'
        verbose_name_plural = 'Постройки'
