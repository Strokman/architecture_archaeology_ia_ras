from django import forms

from arch_site.models import ArchaeologicalSite
from core.custom_forms import FileMixinForm, ArchaeologicalObjectFormMixin


class SubmitBuildingForm(ArchaeologicalObjectFormMixin, FileMixinForm):
    site = forms.ModelChoiceField(label='Памятник', queryset=ArchaeologicalSite.objects.all())
