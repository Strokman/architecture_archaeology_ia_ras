from django import forms
from measurement.models import ScanningElectronMicroscopy

from core.custom_forms import FileFormMixin, BaseDateInputMeta, OtherFilesFormMixin


class SubmitScanningMicroscopyForm(forms.ModelForm, OtherFilesFormMixin, FileFormMixin):

    report = forms.FileField(required=False, label='Результат', help_text='Файл отчета об анализе')

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
            'report',
            'other'
        )
