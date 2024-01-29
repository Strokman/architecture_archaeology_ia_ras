from artefact.models import Artefact
from artefact.filter import ArtefactFilter
from core.view_mixins import ListViewMixin


class ListArtefactView(ListViewMixin):
    filterset_class = ArtefactFilter
    model = Artefact
