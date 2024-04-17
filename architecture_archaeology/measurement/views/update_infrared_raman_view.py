from measurement.models import InfraredRamanMicroscopy
from measurement.forms import SubmitInfraredRamanForm
from core.view_mixins import UpdateMeasurementMixin


class UpdateInfraredRamanView(UpdateMeasurementMixin):
    model = InfraredRamanMicroscopy
    form_class = SubmitInfraredRamanForm