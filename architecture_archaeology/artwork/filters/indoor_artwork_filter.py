from artwork.filters import ArtworkBaseFilter
from artwork.models import IndoorArtwork


class IndoorArtworkFilter(ArtworkBaseFilter):

    class Meta:
        model = IndoorArtwork
        fields = []
