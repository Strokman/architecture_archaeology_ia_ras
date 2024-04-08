from django import forms
from measurement.models import InfraredRamanMicroscopy

from core.custom_forms import FileFormMixin, BaseDateInputMeta, CodeMixin


class SubmitInfraredRamanForm(forms.ModelForm, FileFormMixin, CodeMixin):

    class Meta(BaseDateInputMeta):
        model = InfraredRamanMicroscopy
        fields = (
            'name',
            'method',
            'groups',
            'measurement_date',
            'material',
            'operator',
            'code',
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
