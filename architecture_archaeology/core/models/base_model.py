from collections.abc import Iterable
from django.db import models
from django.urls import reverse_lazy
from logging import getLogger
import architecture_archaeology.settings as settings


class BaseModel(models.Model):

    """
    Базовая модель, попытка ввести логирование. Остальное - стандартно.
    При желании можно расширить функционал.
    """
    def __init__(self, *args: reverse_lazy, **kwargs: reverse_lazy) -> None:
        self.logger = getLogger(settings.PROJECT + '.' + self.__class__.__name__)
        super().__init__(*args, **kwargs)

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        super().save()
        
        self.logger.info(f'{self} saved')

    def delete(self, *args, **kwargs) -> tuple[int, dict[str, int]]:
        self.logger.info(f'{self} deleted')
        return super().delete(*args, **kwargs)

    def get_absolute_url(self):
        """
        Переопределен метод для того, чтобы подходил для большей части моделей.
        Если есть slug - используется он. Если нет - айдишник.
        Так как в url в основном используется название приложения и модели - то
        они используются для генерации абсолютных путей.
        В некоторых моделях по своему прописан этот метод.
        """
        app = self._meta.app_label
        model_name = self.__class__.__name__.lower()
        if hasattr(self, 'slug'):
            return reverse_lazy(f"{self._meta.app_label}:detail{"-" + model_name if app in ['artwork', 'measurement'] else ""}", kwargs={"slug": self.slug})
        return reverse_lazy(f"{self._meta.app_label}:detail{"-" + model_name if app in ['artwork', 'measurement'] else ""}", kwargs={"pk": self.pk})

    class Meta:
        abstract = True
