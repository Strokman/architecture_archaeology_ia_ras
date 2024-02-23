from django import forms
from measurement.models import ScanningElectronMicroscopy

from core.custom_forms import FileFormMixin, BaseDateInputMeta


class SubmitScanningMicroscopyForm(forms.ModelForm, FileFormMixin):

    # report = forms.FileField(required=False, label='Результат', help_text='Файл отчета об анализе')

    class Meta(BaseDateInputMeta):
        model = ScanningElectronMicroscopy
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
            'elements',
            'source',
            'comment',
            'foto',
            'other'
        )
