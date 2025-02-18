from django.core.files.uploadedfile import (TemporaryUploadedFile,
                                            InMemoryUploadedFile)
from django.apps import apps
from uuid import uuid4
import os
from file.services.file_to_s3 import S3FileHandler

from django.db import models


class FileHandler:
    """
    Для обработки файлов создан класс.
    Атрибуты:
    file - загруженный файл в формате джанго
    parent_obj - модель, к которой привязывается файл
    model - модель файла (фото или другое на данный момент)
    filename - имя файла, формируется из uuid4 и расширения,
    чтобы избежать повторений
    original_fileneme - оригинальное название от пользвотеля,
    под ним файл отдается на скачивание и для отображения в темплейтах
    """

    def __init__(self,
                 file: TemporaryUploadedFile | InMemoryUploadedFile,
                 parent_obj, model: str) -> None:
        self.file = file
        self.parent_obj = parent_obj
        self.model = model
        self.filename = f'{uuid4()}{self.extension}'

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        if isinstance(file, (TemporaryUploadedFile, InMemoryUploadedFile)):
            self.__file = file
        else:
            raise ValueError('File Object is not supported')

    @property
    def parent_obj(self):
        return self._parent_obj

    @parent_obj.setter
    def parent_obj(self, parent_obj):
        if not isinstance(parent_obj, models.Model):
            raise ValueError('Parent object should be of type Django Model')
        self._parent_obj = parent_obj

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        try:
            self.__model = apps.get_model('file', model)
        except LookupError:
            raise ValueError('No such file type')

    @property
    def extension(self):
        rv = os.path.splitext(self.file.name)[1]
        return rv

    @property
    def original_filename(self):
        original_filename = os.path.splitext(
            self.file.name)[0].replace('/', '-').replace('.', '-')
        return original_filename + self.extension

    @property
    def object_storage_key(self):
        """
        Путь, по которому сохраняется в S3 файл. Также служит как
        ключ, по которому получается доступ к файлу
        """
        return f'{self.parent_obj._meta.db_table}/{self.parent_obj.id}/{self.model._meta.model_name}/{self.filename}'

    def to_orm(self):
        """
        Сохраняет данные о файле в БД
        и одновременно сохраняет в S3.
        По нормальному конечно нужно изменить, чтобы 
        методы делали что-то одно.
        """
        uploader = S3FileHandler(self)
        instance = self.model(filename=self.filename,
                            extension=self.extension,
                            original_name=self.original_filename,
                            object_storage_key=self.object_storage_key
                            )
        uploader.upload_file_to_s3()
        instance.save()
        attr = getattr(self.parent_obj, f'{self.model._meta.model_name}_set')
        attr.add(instance)
        return True
