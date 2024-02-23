from django import forms


class YearValidationMixin:

    def clean(self):
        if self.cleaned_data['year_min'] > self.cleaned_data['year_max']:
            raise forms.ValidationError('Конец интервала датировки не может быть больше его начала')
        return super().clean()