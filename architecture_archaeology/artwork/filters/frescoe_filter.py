import django_filters
from django import forms

from artwork.models import Frescoe, IndoorArtwork
from artwork.filters import ArtworkBaseFilter
from helpers.models import Storage


class FrescoeFilter(ArtworkBaseFilter):
    storage = django_filters.ModelMultipleChoiceFilter(
        queryset=Storage.objects.all()
        )
    indoor_artwork = django_filters.ModelMultipleChoiceFilter(
        queryset=IndoorArtwork.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10})
        )

    class Meta:
        model = Frescoe
        fields = ['type']
