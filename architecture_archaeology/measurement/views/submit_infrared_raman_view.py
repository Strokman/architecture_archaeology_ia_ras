from measurement.models import InfraredRamanMicroscopy
from measurement.forms import SubmitInfraredRamanForm
from core.view_mixins import CreateViewMixin


class SubmitInfraredRamanView(CreateViewMixin):

    model = InfraredRamanMicroscopy
    form_class = SubmitInfraredRamanForm
