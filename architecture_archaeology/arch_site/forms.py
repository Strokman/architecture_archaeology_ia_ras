from django import forms
from helpers.models import Region


class SubmitArchaeologicalSiteForm(forms.Form):
    name = forms.CharField(label='Название')
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    region = forms.ModelChoiceField(label='Регион', queryset=Region.objects.all())
    long = forms.DecimalField(label='Долгота')
    lat = forms.DecimalField(label='Широта')
    year_min = forms.IntegerField(label='от')
    year_max = forms.IntegerField(label='до')
    comment = forms.CharField(widget=forms.Textarea)
    # foto = forms.FileField(label='Фотография')