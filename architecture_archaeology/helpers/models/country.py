from django.db import models
from core.models import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ('name', 'id')
