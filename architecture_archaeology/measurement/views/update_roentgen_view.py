from measurement.models import Roentgen
from measurement.forms import SubmitRoentgenForm
from core.view_mixins import UpdateMeasurementMixin


class UpdateRoentgenView(UpdateMeasurementMixin):
    model = Roentgen
    form_class = SubmitRoentgenForm
