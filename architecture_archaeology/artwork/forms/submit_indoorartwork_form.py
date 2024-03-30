from django import forms
from artwork.models import IndoorArtwork
from core.custom_forms import FileFormMixin, YearValidationMixin


class SubmitIndoorArtworkForm(YearValidationMixin, forms.ModelForm, FileFormMixin):

    class Meta:
        model = IndoorArtwork
        fields = ('name',
                  'description',
                  'year_min',
                  'year_max',
                  'find_date_from',
                  'find_date_to',
                  'comment',
                  'site',
                  'color',
                  'preservation',
                  'foto',
                  'other')