from django.db import models
from core.base_model import BaseModel


class DescriptionMixin(BaseModel):

    description = models.TextField(null=False, verbose_name='Описание')

    # def save(self, *args, **kwargs):
    #     assert self.description, "Field should not be empty."
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.description}'

    class Meta:

        abstract = True
