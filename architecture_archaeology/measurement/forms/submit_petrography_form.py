from django import forms
from measurement.models import Petrography
from helpers.models import Filler
from core.custom_forms import (
    FileFormMixin,
    BaseDateInputMeta,
    CodeMixin, ColorMixin
    )


class SubmitPetrographyForm(forms.ModelForm,
                            FileFormMixin,
                            CodeMixin,
                            ColorMixin):
    filler_contains = forms.ModelMultipleChoiceField(
        label='Заполнитель состав',
        required=False,
        queryset=Filler.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 8}),
        help_text='Для множественного выбора используйте Shift + левая кнопка мыши'
        )
    
    class Meta(BaseDateInputMeta):
        model = Petrography
        fields = (
            'name',
            'number',
            'measurement_date',
            'operator',
            'code',
            'equipment',
            'binder_name',
            'binder_percent',
            'binder_description',
            'filler_percent',
            'filler_contains',
            'filler_description',
            'color',
            'pores',
            'pores_diameter',
            'comment',
            'foto',
            'other'
        )
