from django.db import models
from core.models import BaseModel


class Country(BaseModel):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'