from typing import Any
from django import forms


class ArchaeologicalObjectFormMixin(forms.Form):
    name = forms.CharField(label='Название')
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    long = forms.DecimalField(label='Долгота')
    lat = forms.DecimalField(label='Широта')
    year_min = forms.IntegerField(label='от')
    year_max = forms.IntegerField(label='до')
    comment = forms.CharField(widget=forms.Textarea)
