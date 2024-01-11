from artefact.models import Artefact
from core.view_mixins import ListViewMixin


class ListArtefactView(ListViewMixin):

    model = Artefact
