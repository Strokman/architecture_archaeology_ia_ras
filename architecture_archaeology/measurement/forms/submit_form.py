
from django import forms
from django.utils import timezone
from measurement.models import RFA
from core.custom_forms import FileFormMixin


class SubmitRFAForm(forms.ModelForm, FileFormMixin):

    class Meta:
        model = RFA
        fields = (
            'name',
            'measurement_date',
            'material',
            'operator',
            'equipment',
            'conditions',
            'color',
            'pigment',
            'additional_elements',
            'source',
            'comment',
            'foto'
        )
        widgets = {
            'measurement_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            )
        }
        
    # def __init__(self, *args, **kwargs):
    #     super(SubmitRFAForm, self).__init__(*args, **kwargs)
    #     self.initial['measurement_date'] = timezone.now()