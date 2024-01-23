from django import forms
from measurement.models import Petrography

from core.custom_forms import FileFormMixin, BaseDateInputMeta, OtherFilesFormMixin


class SubmitPetrographyForm(forms.ModelForm, OtherFilesFormMixin, FileFormMixin):

    class Meta(BaseDateInputMeta):
        model = Petrography
        fields = (
            'name',
            'number',
            'measurement_date',
            'operator',
            'equipment',
            'binder_name',
            'binder_percent',
            'binder_description',
            'filler_percent',
            'filler_contains',
            'filler_description',
            'pores',
            'pores_diameter',
            'comment',
            'foto',
            'other'
        )
