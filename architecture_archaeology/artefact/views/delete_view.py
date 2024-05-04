from artefact.models import Artefact
from core.view_mixins import DeleteViewMixin


class DeleteArtefactView(DeleteViewMixin):
    model = Artefact