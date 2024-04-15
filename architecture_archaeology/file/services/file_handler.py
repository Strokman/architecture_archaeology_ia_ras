from django.core.files.uploadedfile import (TemporaryUploadedFile,
                                            InMemoryUploadedFile)
from django.apps import apps
from uuid import uuid4
import os
# from dataclasses import dataclass
from file.services.file_to_s3 import S3FileHandler

from django.db import models


# @dataclass
# class FileDTO:
#     filename: str
#     extension: str
#     original_name: str
#     file_stream: TemporaryUploadedFile | InMemoryUploadedFile


class FileHandler:

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
            self.file.name)[0].replace('/','-').replace('.', '-')
        return original_filename + self.extension

    @property
    def object_storage_key(self):
        return f'{self.parent_obj._meta.db_table}/{self.model._meta.model_name}/{self.parent_obj.id}/{self.filename}'

    def to_orm(self):
        uploader = S3FileHandler(self)
        # if self.model.name in ('фотография', 'отчет', 'план'):
        #     try:
        #         instance: models.Model = self.parent_obj.file_set.get(type=self.model)
        #         old_file_in_s3 = S3FileHandler(instance)
        #         old_file_in_s3.delete_file_from_s3()
        #         instance.filename = self.filename
        #         instance.extension = self.extension
        #         instance.original_name = self.original_filename
        #         instance.type = self.model
        #         instance.object_storage_key = self.object_storage_key
        #         uploader.upload_file_to_s3()
        #         instance.save()  
        #         return True
        #     except File.DoesNotExist:
        #         pass
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
