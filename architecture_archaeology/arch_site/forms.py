from django import forms
from arch_site.models import ArchaeologicalSite
from core.custom_forms import (
                            FileFormMixin,
                            YearValidationMixin
                            )


class SubmitArchaeologicalSiteForm(
                                YearValidationMixin,
                                forms.ModelForm,
                                FileFormMixin
                                ):

    class Meta:
        model = ArchaeologicalSite
        fields = (
            'name',
            'description',
            'lat',
            'long',
            'preservation',
            'year_min',
            'year_max',
            'comment'
            )
