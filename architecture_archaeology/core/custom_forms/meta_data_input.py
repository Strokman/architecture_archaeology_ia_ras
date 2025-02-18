from django import forms


class BaseDateInputMeta:
    """
    Переопределние поля дат для корректного отображения в темплейтах
    """
    widgets = {
        'measurement_date': forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date', 'class': 'form-control'}
        )
    }