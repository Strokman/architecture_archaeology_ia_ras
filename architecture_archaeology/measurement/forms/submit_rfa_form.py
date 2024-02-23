from django import forms
# from django.core import validators
from measurement.models import RFA
from core.custom_forms import FileFormMixin, BaseDateInputMeta


class SubmitRFAForm(forms.ModelForm, FileFormMixin):

    # report = forms.FileField(required=False, label='Результат', help_text='Файл отчета об анализе')

    # other = forms.FileField(required=False, label='Спектр', validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], help_text='Обработанный спектр. Допустимые форматы: .png, .jpg')

    class Meta(BaseDateInputMeta):
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
            'foto',
            'other'
        )
