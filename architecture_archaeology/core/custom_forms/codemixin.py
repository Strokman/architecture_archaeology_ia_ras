from django import forms


class CodeMixin(forms.Form):
    """
    Поле шифр (code) используется во многих моделях,
    поэтому сделал такой класс для добавления поля шифр
    во все формы, где такие модели используются
    """

    code = forms.IntegerField(
        min_value=1,
        required=True,
        label='Шифр объекта',
        help_text='Шифр фрески/артефакта для привязки'
        )
