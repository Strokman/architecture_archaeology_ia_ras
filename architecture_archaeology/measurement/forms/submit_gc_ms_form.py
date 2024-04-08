from django import forms
from measurement.models import GasChromatographyMassSpectrometry

from core.custom_forms import FileFormMixin, BaseDateInputMeta

from core.custom_forms import CodeMixin


class SubmitGCMSForm(forms.ModelForm, FileFormMixin, CodeMixin):

    class Meta(BaseDateInputMeta):
        model = GasChromatographyMassSpectrometry
        fields = (
            'name',
            'measurement_date',
            'material',
            'operator',
            'equipment',
            'code',
            'conditions',
            'color',
            'pigment',
            'additional_elements',
            'source',
            'comment',
            'foto',
            'other'
        )
