from django import forms


class YearValidationMixin:
    """
    Миксин для валидации ввода пользователя, чтобы нельзя было ввести год начала интервала больше,
    чем конец интервала или наоборот.
    """

    def clean(self):
        if not self.cleaned_data.get('year_min') and not self.cleaned_data.get('year_max'):
            return super().clean()
        min = self.cleaned_data.get('year_min') if self.cleaned_data.get('year_min') else -10000
        max = self.cleaned_data.get('year_max') if self.cleaned_data.get('year_max') else 2024
        if min > max:
            raise forms.ValidationError('Конец интервала датировки не может быть больше его начала')
        return super().clean()