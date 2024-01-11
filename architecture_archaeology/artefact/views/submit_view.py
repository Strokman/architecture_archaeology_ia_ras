from artefact.models import Artefact
from artefact.forms import SubmitArtefactForm

from core.view_mixins import CreateViewMixin


class SubmitArtefactView(CreateViewMixin):
    model = Artefact
    form_class = SubmitArtefactForm
