from measurement.models import RFA
from measurement.forms import SubmitRFAForm
from core.view_mixins import UpdateMeasurementMixin


class UpdateRFAView(UpdateMeasurementMixin):
    model = RFA
    form_class = SubmitRFAForm
