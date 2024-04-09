from django import forms
from measurement.models import Roentgen

from helpers.models import Mineral

from core.custom_forms import FileFormMixin, BaseDateInputMeta, CodeMixin


class SubmitRoentgenForm(forms.ModelForm, FileFormMixin, CodeMixin):

    mineral = forms.ModelMultipleChoiceField(
        label='Минералы',
        required=False,
        queryset=Mineral.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10}))

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
