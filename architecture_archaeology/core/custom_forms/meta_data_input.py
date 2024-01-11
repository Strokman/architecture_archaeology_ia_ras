from django import forms


class BaseDateInputMeta:
    widgets = {
        'measurement_date': forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        )
    }