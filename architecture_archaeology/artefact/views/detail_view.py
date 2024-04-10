from artefact.models import Artefact
from core.view_mixins import DetailViewMixin


class DetailArtefactView(DetailViewMixin):
    model = Artefact
    template_name = 'artefact/detail.html'
