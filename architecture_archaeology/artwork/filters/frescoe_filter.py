import django_filters
from arch_site.models import ArchaeologicalSite
from building.models import Building, BuildingPart
from artwork.models import Frescoe, IndoorArtwork
from helpers.models import Color, Preservation, Storage
from core.filters import RangeDatesFilterBase
from artwork.filters import ArtworkBaseFilter

class FrescoeFilter(ArtworkBaseFilter):
    storage = django_filters.ModelMultipleChoiceFilter(queryset=Storage.objects.all())
    indoor_artwork = django_filters.ModelMultipleChoiceFilter(queryset=IndoorArtwork.objects.all())

    class Meta:
        model = Frescoe
        fields = ['type']
