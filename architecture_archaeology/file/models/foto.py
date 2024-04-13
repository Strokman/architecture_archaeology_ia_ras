from django.db import models
from core.models import TimestampMixin


class Foto(TimestampMixin):
    filename = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    object_storage_key = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.filename

    class Meta:

        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ('id', )