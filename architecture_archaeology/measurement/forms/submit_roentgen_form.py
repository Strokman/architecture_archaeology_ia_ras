from django import forms
from measurement.models import Roentgen

from helpers.models import Mineral, Color, Pigment

from core.custom_forms import FileFormMixin, BaseDateInputMeta, CodeMixin


class SubmitRoentgenForm(forms.ModelForm, FileFormMixin, CodeMixin):
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
    mineral = forms.ModelMultipleChoiceField(
        label='Минералы',
        required=False,
        queryset=Mineral.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10}),
        help_text='Для множественного выбора используйте Shift + левая кнопка мыши'
        )

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
