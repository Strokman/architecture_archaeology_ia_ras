from core.view_mixins import UpdateViewMixin

from artefact.models import Artefact
from artefact.forms import SubmitArtefactForm


class UpdateArtefactView(UpdateViewMixin):

    model = Artefact
    form_class = SubmitArtefactForm
