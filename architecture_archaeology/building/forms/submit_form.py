from django import forms
from django.core import validators

from building.models import Building
from core.custom_forms import MultipleFileField


class SubmitBuildingForm(forms.ModelForm):
    foto = MultipleFileField(5, validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], label='Фотография')

    class Meta:

        model = Building
        fields = ['name', 'description', 'site', 'long', 'lat', 'year_min', 'year_max', 'comment']
