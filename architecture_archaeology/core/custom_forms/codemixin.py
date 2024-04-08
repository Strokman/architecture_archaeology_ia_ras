from django import forms


class CodeMixin(forms.Form):

    code = forms.IntegerField(
        min_value=1,
        required=True,
        label='Шифр объекта',
        help_text='Шифр фрески/артефакта для привязки'
        )
