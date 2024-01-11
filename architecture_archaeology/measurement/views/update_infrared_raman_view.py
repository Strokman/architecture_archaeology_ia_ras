from measurement.models import InfraredRamanMicroscopy
from measurement.forms import SubmitInfraredRamanForm
from core.view_mixins import UpdateViewMixin


class UpdateInfraredRamanView(UpdateViewMixin):
    model = InfraredRamanMicroscopy
    form_class = SubmitInfraredRamanForm