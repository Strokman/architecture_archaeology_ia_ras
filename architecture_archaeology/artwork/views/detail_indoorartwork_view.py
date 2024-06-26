from artwork.models import IndoorArtwork
from core.view_mixins import DetailViewMixin


class DetailIndoorArtworkView(DetailViewMixin):
    model = IndoorArtwork
    template_name = 'indoor_artwork/detail.html'
