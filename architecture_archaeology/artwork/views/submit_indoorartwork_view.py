from artwork.models import IndoorArtwork
from artwork.forms import SubmitIndoorArtworkForm

from core.view_mixins import CreateViewMixin


class SubmitIndoorArtworkView(CreateViewMixin):
    model = IndoorArtwork
    form_class = SubmitIndoorArtworkForm
    template_name = 'submit.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
