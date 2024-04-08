from measurement.models import InfraredRamanMicroscopy
from measurement.forms import SubmitInfraredRamanForm
from core.view_mixins import CreateMeasurementMixin


class SubmitInfraredRamanView(CreateMeasurementMixin):

    model = InfraredRamanMicroscopy
    form_class = SubmitInfraredRamanForm
