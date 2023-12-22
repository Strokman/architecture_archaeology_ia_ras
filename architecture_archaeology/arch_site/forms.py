from django import forms
from django.core import validators
from core.custom_forms import MultipleFileField
from arch_site.models import ArchaeologicalSite


class SubmitArchaeologicalSiteForm(forms.ModelForm):
    foto = MultipleFileField(5, validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], label='Фотография')
    plan = forms.FileField(required=False, validators=[validators.FileExtensionValidator(['pdf', 'tif', 'tiff', 'jpg', 'jpeg'])], label='План')

    class Meta:
        model = ArchaeologicalSite
        fields = ['name', 'description', 'region', 'long', 'lat', 'year_min', 'year_max', 'comment']
