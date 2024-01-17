from django.core.files.uploadedfile import (TemporaryUploadedFile,
                                            InMemoryUploadedFile)

from uuid import uuid4
import os
# from dataclasses import dataclass
from file.models import File, FileType
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
                 parent_obj, file_type: str) -> None:
        self.file = file
        self.parent_obj = parent_obj
        self.file_type = file_type
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
    def file_type(self):
        return self.__file_type

    @file_type.setter
    def file_type(self, file_type):
        try:
            self.__file_type = FileType.objects.get(name=file_type)
        except FileType.DoesNotExist:
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
        return f'{self.parent_obj._meta.db_table}/{self.parent_obj.id}/{self.filename}'

    def to_orm(self):
        uploader = S3FileHandler(self)
        if self.file_type.name in ('фотография', 'отчет', 'план'):
            try:
                instance: models.Model = self.parent_obj.file_set.get(type=self.file_type)
                old_file_in_s3 = S3FileHandler(instance)
                old_file_in_s3.delete_file_from_s3()
                instance.filename = self.filename
                instance.extension = self.extension
                instance.original_name = self.original_filename
                instance.type = self.file_type
                instance.object_storage_key = self.object_storage_key
                uploader.upload_file_to_s3()
                instance.save()  
                return True
            except File.DoesNotExist:
                pass
        instance = File(filename=self.filename,
                        extension=self.extension,
                        original_name=self.original_filename,
                        type=self.file_type,
                        object_storage_key=self.object_storage_key
                        )       
        uploader.upload_file_to_s3()
        instance.save()
        self.parent_obj.file_set.add(instance)
        return True

    # @classmethod
    # def from_orm(cls, **kwargs):
    #     try:
    #         file = cls.objects.get(**kwargs)
    #         return file
    #     except:
    #         raise FileNotFoundError('No such file')

