from django import forms
from artwork.models import IndoorArtwork
from core.custom_forms import FileFormMixin


class SubmitIndoorArtworkForm(forms.ModelForm, FileFormMixin):

    class Meta:
        model = IndoorArtwork
        fields = ('name',
                  'description',
                  'code',
                  'year_min',
                  'year_max',
                  'find_date_from',
                  'find_date_to',
                  'square_number',
                  'comment',
                  'building',
                  'building_part',
                  'color',
                  'preservation',
                  'foto')