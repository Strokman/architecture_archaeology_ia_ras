from django import forms
from artwork.models import Lotok
from core.custom_forms import FileFormMixin, YearValidationMixin


class SubmitLotokForm(YearValidationMixin, forms.ModelForm, FileFormMixin):

    class Meta:
        model = Lotok
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
                  'foto',
                  'other')
