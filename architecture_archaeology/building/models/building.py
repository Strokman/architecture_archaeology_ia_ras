from django.db import models
from core.timestamp_mixin import TimestampMixin
from core.description_mixin import DescriptionMixin


class Building(DescriptionMixin, TimestampMixin):

    name = models.CharField(max_length=255)
    long = models.DecimalField(max_digits=23, decimal_places=20)
    lat = models.DecimalField(max_digits=23, decimal_places=20)

    comment_id = models.ForeignKey('helpers.Comment', null=True, on_delete=models.CASCADE)
    date_id = models.ForeignKey('helpers.Date', null=True, on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Постройка'
        verbose_name_plural = 'Постройки'

    def __str__(self):
        return f'{self.name}'
