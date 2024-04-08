from measurement.models import Petrography
from measurement.forms import SubmitPetrographyForm

from core.view_mixins import CreateMeasurementMixin


class SubmitPetrographyView(CreateMeasurementMixin):
    model = Petrography
    form_class = SubmitPetrographyForm