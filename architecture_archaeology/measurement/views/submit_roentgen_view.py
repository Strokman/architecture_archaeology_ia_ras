from measurement.models import Roentgen
from measurement.forms import SubmitRoentgenForm

from core.view_mixins import CreateMeasurementMixin


class SubmitRoentgenView(CreateMeasurementMixin):
    model = Roentgen
    form_class = SubmitRoentgenForm