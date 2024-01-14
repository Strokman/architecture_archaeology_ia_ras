from django.db import models


class FileType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:

        verbose_name = 'Тип файла'
        verbose_name_plural = 'Типы файлов'
        ordering = ('name', )
