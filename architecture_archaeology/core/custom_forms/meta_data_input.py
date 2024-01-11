from django import forms


class BaseDateInputMeta:
    widgets = {
        'measurement_date': forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date', 'class': 'form-control'}
        )
    }