from collections.abc import Iterable
from django.db import models
from logging import getLogger
import architecture_archaeology.settings as settings


class BaseModel(models.Model):

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:  
        logger = getLogger(settings.PROJECT + '.' + self.__class__.__name__)
        logger.info(f'{self} saved')
        super().save()

    class Meta:
        abstract = True
