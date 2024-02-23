from django import forms
from measurement.models import GasChromatographyMassSpectrometry

from core.custom_forms import FileFormMixin, BaseDateInputMeta


class SubmitGCMSForm(forms.ModelForm, FileFormMixin):

    class Meta(BaseDateInputMeta):
        model = GasChromatographyMassSpectrometry
        fields = (
            'name',
            'measurement_date',
            'material',
            'operator',
            'equipment',
            'conditions',
            'color',
            'pigment',
            'additional_elements',
            'source',
            'comment',
            'foto',
            'other'
        )
