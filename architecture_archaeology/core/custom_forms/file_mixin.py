from django import forms
from core.custom_forms import MultipleFileField
from django.core import validators


class FileMixinForm(forms.Form):
    foto = MultipleFileField(5, validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], label='Фотография')
    plan = forms.FileField(required=True, validators=[validators.FileExtensionValidator(['pdf', 'tif', 'tiff', 'jpg', 'jpeg'])], label='План')