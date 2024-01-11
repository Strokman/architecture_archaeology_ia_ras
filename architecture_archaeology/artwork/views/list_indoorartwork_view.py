from artwork.models import IndoorArtwork
from core.view_mixins import ListViewMixin


class ListIndoorArtworkView(ListViewMixin):

    model = IndoorArtwork
