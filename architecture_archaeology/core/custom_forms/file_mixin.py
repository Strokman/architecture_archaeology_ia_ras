from typing import Any
from django import forms
from core.custom_forms import MultipleFileField
from django.core import validators
from core.exceptions import FilesNumberValidationError


# class MultipleFileFormMixin(forms.Form):
    # foto = MultipleFileField(5, validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], label='Фотографии', help_text='Допустимые форматы: .png, .jpg')
    # foto = forms.FileField(required=False, validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], label='Фотография', help_text='Допустимые форматы: .png, .jpg')

# class MaxFilesValidator:
#     counter = 0

#     def __call__(self):
#         self.counter += 1


class FileFormMixin(forms.Form):
    
    foto = MultipleFileField(3, required=False, validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], label='Фотографии', help_text='Не более 3 файлов. Допустимые форматы: .png, .jpg')
    other = MultipleFileField(10, required=False, label='Другие файлы', help_text='Не более 10 файлов')
