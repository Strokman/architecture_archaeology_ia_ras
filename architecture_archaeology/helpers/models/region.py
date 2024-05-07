from django.db import models
from core.models import BaseModel


class Region(BaseModel):
    name = models.CharField(max_length=200)

    country = models.ForeignKey('helpers.Country', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country}, {self.name}'

    class Meta:
        verbose_name = verbose_name_plural = 'Административная принадлежность'
        ordering = ('country', 'name')
