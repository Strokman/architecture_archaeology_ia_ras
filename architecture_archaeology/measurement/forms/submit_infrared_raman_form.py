from django import forms
from measurement.models import InfraredRamanMicroscopy

from core.custom_forms import FileFormMixin, BaseDateInputMeta


class SubmitInfraredRamanForm(forms.ModelForm, FileFormMixin):

    class Meta(BaseDateInputMeta):
        model = InfraredRamanMicroscopy
        fields = (
            'name',
            'method',
            'groups',
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
