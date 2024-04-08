from collections.abc import Iterable
from django.db import models
from django.urls import reverse_lazy
from logging import getLogger
import architecture_archaeology.settings as settings


class BaseModel(models.Model):

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        super().save()
        logger = getLogger(settings.PROJECT + '.' + self.__class__.__name__)
        logger.info(f'{self} saved')

    def get_absolute_url(self):
        app = self._meta.app_label
        model_name = self.__class__.__name__.lower()
        if hasattr(self, 'slug'):
            return reverse_lazy(f"{self._meta.app_label}:detail{"-" + model_name if app in ['artwork', 'measurement'] else ""}", kwargs={"slug": self.slug})
        return reverse_lazy(f"{self._meta.app_label}:detail{"-" + model_name if app in ['artwork', 'measurement'] else ""}", kwargs={"pk": self.pk})

    class Meta:
        abstract = True
