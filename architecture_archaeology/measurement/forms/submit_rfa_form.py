from django import forms
# from django.core import validators
from measurement.models import RFA
from helpers.models import Element, Color, Pigment
from core.custom_forms import FileFormMixin, BaseDateInputMeta
from core.custom_forms import CodeMixin


class SubmitRFAForm(forms.ModelForm, FileFormMixin, CodeMixin):

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
        model = RFA
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
            'elements',
            'additional_elements',
            'source',
            'comment',
            'foto',
            'other'
        )
