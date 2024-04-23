from typing import Any
from django import forms
from core.custom_forms import MultipleFileField
from django.core import validators


class FileFormMixin(forms.Form):
    
    foto = MultipleFileField(3,
                             required=False,
                             validators=[validators.FileExtensionValidator(
                                 ['png', 'jpg', 'jpeg'])
                                 ],
                             label='Фотографии',
                             help_text='Не более 3 файлов. \
                                Размер одного файла - не более 40 мб.\
                                Допустимые форматы: .png, .jpg. \
                                Первый выбранный файл будет использован\
                                в качестве превью'
                                )
    other = MultipleFileField(10,
                              required=False,
                              label='Другие файлы',
                              help_text='Не более 10 файловю\
                              Размер одного файла - не более 40 мб.'
                              )
