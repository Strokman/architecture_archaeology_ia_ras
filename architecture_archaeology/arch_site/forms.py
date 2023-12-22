from django import forms
# from helpers.models import Region
from django.core import validators
from core.custom_forms import MultipleFileField
# from core.custom_forms import ArchaeologicalObjectFormMixin
from arch_site.models import ArchaeologicalSite


# class SubmitArchaeologicalSiteForm(ArchaeologicalObjectFormMixin):
#     field_order = ['name', 'description', 'region']
#     region = forms.ModelChoiceField(label='Регион', queryset=Region.objects.all())
#     foto = MultipleFileField(5, validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], label='Фотография')
#     plan = forms.FileField(required=True, validators=[validators.FileExtensionValidator(['pdf', 'tif', 'tiff', 'jpg', 'jpeg'])], label='План')


class SubmitArchaeologicalSiteForm(forms.ModelForm):
    foto = MultipleFileField(5, validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], label='Фотография')

    class Meta:
        model = ArchaeologicalSite
        fields = ['name', 'description', 'region', 'long', 'lat', 'year_min', 'year_max', 'comment', 'foto']
