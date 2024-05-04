from artwork.models import IndoorArtwork
from core.view_mixins import DeleteViewMixin


class DeleteIndoorArtworkView(DeleteViewMixin):
    model = IndoorArtwork
