from django import forms
from measurement.models import Roentgen

from core.custom_forms import FileFormMixin, BaseDateInputMeta, OtherFilesFormMixin


class SubmitRoentgenForm(forms.ModelForm, OtherFilesFormMixin, FileFormMixin):

    class Meta(BaseDateInputMeta):
        model = Roentgen
        fields = (
            'name',
            'measurement_date',
            'material',
            'operator',
            'equipment',
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