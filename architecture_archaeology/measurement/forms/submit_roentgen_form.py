from django import forms
from measurement.models import Roentgen

from core.custom_forms import FileFormMixin, BaseDateInputMeta, CodeMixin


class SubmitRoentgenForm(forms.ModelForm, FileFormMixin, CodeMixin):

    class Meta(BaseDateInputMeta):
        model = Roentgen
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
            'mineral',
            'additional_elements',
            'source',
            'comment',
            'foto',
            'other'
        )
