from django import forms
from artwork.models import Frescoe
from core.custom_forms import FileFormMixin


class SubmitFrescoeForm(forms.ModelForm, FileFormMixin):

    class Meta:
        model = Frescoe
        fields = ('name',
                  'type',
                  'description',
                  'code',
                  'year_min',
                  'year_max',
                  'find_date_from',
                  'find_date_to',
                  'size',
                  'amount',
                  'museum_code',
                  'square_number',
                  'comment',
                  'indoor_artwork',
                  'building',
                  'building_part',
                  'color',
                  'preservation',
                  'storage',
                  'foto')
