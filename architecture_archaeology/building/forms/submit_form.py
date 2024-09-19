from django import forms

from building.models import Building
from core.custom_forms import FileFormMixin, YearValidationMixin


class SubmitBuildingForm(
                      YearValidationMixin,
                      forms.ModelForm,
                      FileFormMixin
                      ):

    class Meta:
        model = Building
        fields = (
            'name',
            'description',
            'site',
            'preservation',
            'lat',
            'long',
            'year_min',
            'year_max',
            'comment'
            )
