from django import forms
from measurement.models import ScanningElectronMicroscopy
from helpers.models import Element

from core.custom_forms import FileFormMixin, BaseDateInputMeta, CodeMixin


class SubmitScanningMicroscopyForm(forms.ModelForm, FileFormMixin, CodeMixin):

    elements = forms.ModelMultipleChoiceField(
        label='Элементы периодической таблицы',
        required=False,
        queryset=Element.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 8})
        )

    class Meta(BaseDateInputMeta):
        model = ScanningElectronMicroscopy
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
            'elements',
            'source',
            'comment',
            'foto',
            'other'
        )
