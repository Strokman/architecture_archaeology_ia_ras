from django import forms
# from django.core import validators
from arch_site.models import ArchaeologicalSite
from core.custom_forms import FileFormMixin, YearValidationMixin


class SubmitArchaeologicalSiteForm(YearValidationMixin, forms.ModelForm, FileFormMixin):
    # plan = forms.FileField(required=False,
    #                        validators=[validators.FileExtensionValidator(
    #                            ['pdf', 'tif', 'tiff', 'jpg', 'jpeg']
    #                            )],
    #                        label='План',
    #                        help_text='Допустимые форматы: .pdf, .tiff, jpg'
    #                        )

    class Meta:
        model = ArchaeologicalSite
        fields = (
            'name',
            'description',
            'lat',
            'long',
            'preservation',
            'year_min',
            'year_max',
            'comment'
            )
