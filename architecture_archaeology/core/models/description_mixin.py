from django.db import models
from core.models.base_model import BaseModel


class DescriptionMixin(BaseModel):

    description = models.TextField(null=False, verbose_name='Описание')

    def __str__(self):
        return f'{self.description}'

    class Meta:

        abstract = True
