from django.db import models
from core.models.base_model import BaseModel


class DescriptionMixin(BaseModel):
    
    """
    Во многих моделях используется поле Описание,
    поэтому сделал этот класс, чтоб от него отнаследоваться.
    """
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.description}'

    class Meta:

        abstract = True
