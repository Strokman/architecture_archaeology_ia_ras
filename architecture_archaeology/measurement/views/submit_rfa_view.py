from measurement.models import RFA
from measurement.forms import SubmitRFAForm

from core.view_mixins import CreateMeasurementMixin


class SubmitRFAView(CreateMeasurementMixin):
    model = RFA
    form_class = SubmitRFAForm
