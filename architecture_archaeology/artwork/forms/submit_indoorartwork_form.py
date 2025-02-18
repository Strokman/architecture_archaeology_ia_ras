from django import forms
from artwork.models import IndoorArtwork
from core.custom_forms import FileFormMixin, YearValidationMixin, BuildingMixin
from helpers.models import Color


class SubmitIndoorArtworkForm(YearValidationMixin, BuildingMixin, FileFormMixin):
    """
    Для поля цвет кастомизирован класс, чтобы увеличить размер окна
    """

    color = forms.ModelMultipleChoiceField(
        label='Цвета',
        required=False,
        queryset=Color.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10}),
        help_text='Для множественного выбора используйте Shift + левая кнопка мыши'
        )

    class Meta:
        model = IndoorArtwork
        fields = ('name',
                  'description',
                  'year_min',
                  'year_max',
                  'find_date_from',
                  'find_date_to',
                  'comment',
                  'site',
                  'building',
                  'building_part',
                  'color',
                  'preservation',
                  'foto',
                  'other')