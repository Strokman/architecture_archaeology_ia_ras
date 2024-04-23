from django import forms
from measurement.models import GasChromatographyMassSpectrometry

from core.custom_forms import FileFormMixin, BaseDateInputMeta

from core.custom_forms import CodeMixin
from helpers.models import Color, Pigment


class SubmitGCMSForm(forms.ModelForm, FileFormMixin, CodeMixin):

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

    class Meta(BaseDateInputMeta):
        model = GasChromatographyMassSpectrometry
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
            'source',
            'comment',
            'foto',
            'other'
        )
