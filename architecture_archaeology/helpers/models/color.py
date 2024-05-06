from django.db import models
from core.models import DescriptionMixin


class Color(DescriptionMixin):
    code = models.CharField(max_length=7, verbose_name='16-ный код')

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        ordering = ('description', 'id')