from django import forms
from measurement.models import Petrography

from core.custom_forms import FileFormMixin, BaseDateInputMeta, CodeMixin


class SubmitPetrographyForm(forms.ModelForm, FileFormMixin, CodeMixin):

    class Meta(BaseDateInputMeta):
        model = Petrography
        fields = (
            'number',
            'measurement_date',
            'operator',
            'code',
            'equipment',
            'binder_name',
            'binder_percent',
            'binder_description',
            'filler_percent',
            'filler_contains',
            'filler_description',
            'color',
            'pores',
            'pores_diameter',
            'comment',
            'foto',
            'other'
        )
