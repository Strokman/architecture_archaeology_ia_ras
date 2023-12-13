from django import forms
from core.custom_forms import MultipleFileField
from django.core import validators
from helpers.models import Region
from arch_site.models import ArchaeologicalSite


class SubmitBuildingForm(forms.Form):
    name = forms.CharField(label='Название')
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    region = forms.ModelChoiceField(label='Регион', queryset=Region.objects.all())
    region = forms.ModelChoiceField(label='Памятник', queryset=ArchaeologicalSite.objects.all())
    long = forms.DecimalField(label='Долгота')
    lat = forms.DecimalField(label='Широта')
    year_min = forms.IntegerField(label='от')
    year_max = forms.IntegerField(label='до')
    comment = forms.CharField(widget=forms.Textarea)
    foto = MultipleFileField(5, validators=[validators.FileExtensionValidator(['pdf', 'tif', 'tiff', 'jpg', 'jpeg']), validators], label='фотография')
