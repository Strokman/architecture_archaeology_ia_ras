from django.db import models
from core.models.base_model import BaseModel


class TimestampMixin(BaseModel):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')

    class Meta:

        abstract = True
