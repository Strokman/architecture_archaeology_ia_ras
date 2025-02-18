import django_filters
from django import forms

from artwork.models import Frescoe, IndoorArtwork
from artwork.filters import ArtworkBaseFilter
from helpers.models import Storage


class FrescoeFilter(ArtworkBaseFilter):
    storage = django_filters.ModelMultipleChoiceFilter(
        queryset=Storage.objects.all()
        )

    class Meta:
        model = Frescoe
        fields = ('type',
                  'name',
                  'code',
                  'site',
                  'building',
                  'indoor_artwork',
                  'dating',
                  'find_date',
                  'color',
                  'preservation',
                  'storage',
                  'description',
                  'comment',
                  'amount',
                  'size',
                  'museum_code',
                  'square_number'
                  )
