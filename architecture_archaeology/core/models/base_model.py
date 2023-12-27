from collections.abc import Iterable
from django.db import models
from django.urls import reverse_lazy
from logging import getLogger
import architecture_archaeology.settings as settings


class BaseModel(models.Model):

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        logger = getLogger(settings.PROJECT + '.' + self.__class__.__name__)
        logger.info(f'{self} saved')
        super().save()

    def get_absolute_url(self):
        if hasattr(self, 'slug'):
            return reverse_lazy(f"{self._meta.app_label}:detail", kwargs={"slug": self.slug})
        return reverse_lazy(f"{self._meta.app_label}:detail", kwargs={"pk": self.pk})

    class Meta:
        abstract = True
