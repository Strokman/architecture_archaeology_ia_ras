from django import forms
from measurement.models import GasChromatographyMassSpectrometry

from core.custom_forms import FileFormMixin, BaseDateInputMeta, OtherFilesFormMixin


class SubmitGCMSForm(forms.ModelForm, OtherFilesFormMixin, FileFormMixin):

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
