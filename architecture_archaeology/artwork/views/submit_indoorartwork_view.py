from artwork.models import IndoorArtwork
from artwork.forms import SubmitIndoorArtworkForm

from core.view_mixins import CreateViewMixin


class SubmitIndoorArtworkView(CreateViewMixin):
    model = IndoorArtwork
    form_class = SubmitIndoorArtworkForm
