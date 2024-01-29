from artwork.models import IndoorArtwork
from core.view_mixins import ListViewMixin
from artwork.filters import IndoorArtworkFilter


class ListIndoorArtworkView(ListViewMixin):
    filterset_class = IndoorArtworkFilter
    model = IndoorArtwork
