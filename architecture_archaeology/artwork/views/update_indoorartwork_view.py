from core.view_mixins import UpdateViewMixin
from artwork.models import IndoorArtwork
from artwork.forms import SubmitIndoorArtworkForm


class UpdateIndoorArtworkView(UpdateViewMixin):

    model = IndoorArtwork
    form_class = SubmitIndoorArtworkForm
    template_name = 'update.html'
