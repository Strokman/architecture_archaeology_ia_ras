from django import forms
from artwork.models import Frescoe
from core.custom_forms import FileFormMixin, YearValidationMixin


class SubmitFrescoeForm(YearValidationMixin, forms.ModelForm, FileFormMixin):

    class Meta:
        model = Frescoe
        fields = ('name',
                  'type',
                  'description',
                  'year_min',
                  'year_max',
                  'find_date_from',
                  'find_date_to',
                  'size',
                  'amount',
                  'museum_code',
                  'square_number',
                  'comment',
                  'site',
                  'indoor_artwork',
                  'color',
                  'preservation',
                  'storage',
                  'foto',
                  'other')
