from django import forms
from artwork.models import Frescoe
from core.custom_forms import FileFormMixin, YearValidationMixin
from helpers.models import Color


class SubmitFrescoeForm(YearValidationMixin, forms.ModelForm, FileFormMixin):

    color = forms.ModelMultipleChoiceField(
        label='Цвета',
        required=False,
        queryset=Color.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 8}),
        help_text='Для множественного выбора используйте Shift + левая кнопка мыши'
        )

    class Meta:
        model = Frescoe
        fields = ('name',
                  'type',
                  'description',
                  'year_min',
                  'year_max',
                  'find_date_from',
                  'find_date_to',
                  'size',
                  'amount',
                  'museum_code',
                  'square_number',
                  'comment',
                  'site',
                  'building',
                  'building_part',
                  'indoor_artwork',
                  'color',
                  'preservation',
                  'storage',
                  'foto',
                  'other')
