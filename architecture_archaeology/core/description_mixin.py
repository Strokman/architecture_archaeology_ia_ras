from django.db import models
from core.base_model import BaseModel


class DescriptionMixin(BaseModel):

    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return f'{self.description}'
    
    class Meta:

        abstract = True