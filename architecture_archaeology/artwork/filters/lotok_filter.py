import django_filters
from artwork.models import Lotok, IndoorArtwork
from helpers.models import Storage
from artwork.filters import ArtworkBaseFilter


class LotokFilter(ArtworkBaseFilter):
    storage = django_filters.ModelMultipleChoiceFilter(queryset=Storage.objects.all())
    indoor_artwork = django_filters.ModelMultipleChoiceFilter(queryset=IndoorArtwork.objects.all())

    class Meta:
        model = Lotok
        fields = []
