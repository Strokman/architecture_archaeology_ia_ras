from django import forms
from core.custom_forms import MultipleFileField
from django.core import validators


class MultipleFileFormMixin(forms.Form):
    foto = MultipleFileField(5, validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], label='Фотографии', help_text='Допустимые форматы: .png, .jpg')


class FileFormMixin(forms.Form):
    foto = forms.FileField(required=False, validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], label='Фотография', help_text='Допустимые форматы: .png, .jpg')