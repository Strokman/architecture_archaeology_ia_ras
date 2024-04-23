from django import forms
from measurement.models import ScanningElectronMicroscopy
from helpers.models import Element, Pigment, Color

from core.custom_forms import FileFormMixin, BaseDateInputMeta, CodeMixin


class SubmitScanningMicroscopyForm(forms.ModelForm, FileFormMixin, CodeMixin):
    color = forms.ModelMultipleChoiceField(
        label='Цвета',
        required=False,
        queryset=Color.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10}),
        help_text='Для множественного выбора используйте Shift + левая кнопка мыши'
        )
    
    pigment = forms.ModelMultipleChoiceField(
        label='Пигменты',
        required=False,
        queryset=Pigment.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10}),
        help_text='Для множественного выбора используйте Shift + левая кнопка мыши'
        )
    
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
