from django import forms

from building.models import Building
from core.custom_forms import MultipleFileFormMixin


class SubmitBuildingForm(forms.ModelForm, MultipleFileFormMixin):

    class Meta:
        model = Building
        fields = ['name', 'description', 'site', 'long', 'lat', 'year_min', 'year_max', 'comment']
