from django import forms
from artefact.models import Artefact
from core.custom_forms import FileFormMixin, YearValidationMixin


class SubmitArtefactForm(YearValidationMixin, forms.ModelForm, FileFormMixin):

    class Meta:
        model = Artefact
        fields = ('name',
                  'description',
                  'site',
                  'code',
                  'year_min',
                  'year_max',
                  'find_date_from',
                  'find_date_to',
                  'square_number',
                  'comment',
                  'storage',
                  'museum_code',
                  'foto',
                  'other')
