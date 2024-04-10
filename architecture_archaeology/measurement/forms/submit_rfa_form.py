from django import forms
# from django.core import validators
from measurement.models import RFA
from helpers.models import Element
from core.custom_forms import FileFormMixin, BaseDateInputMeta
from core.custom_forms import CodeMixin


class SubmitRFAForm(forms.ModelForm, FileFormMixin, CodeMixin):

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
