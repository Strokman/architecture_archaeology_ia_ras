from django import forms
from helpers.models import Color


class ColorMixin(forms.Form):
    """
    Поле Цвет используется во многих моделях,
    поэтому сделал такой класс для добавления поля цвета
    во все формы, где такие модели используются
    """
    color = forms.ModelMultipleChoiceField(
        label='Цвета',
        required=False,
        queryset=Color.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10}),
        help_text='Для множественного выбора используйте Shift + левая кнопка мыши'
        )