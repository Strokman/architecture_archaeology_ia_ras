from typing import Any
from django import forms
from core.custom_forms import MultipleFileField
from django.core import validators


class FileFormMixin(forms.Form):
    """
    Миксин для форм, который предусматривает добавление полей
    Фото и Другой (файл). По ТЗ ко всем моделям добавляется файлы фото (не более 3-х)
    и Других файлов - не более 10. С лимитом 40 мб. Валидация предусмотрена в классе
    MultipleFileField. Количество допустимых файлов можно изменить первым передавамым
    аргументом при инициализации этого поля. Все остальное в соотв. с Django
    """
    
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
