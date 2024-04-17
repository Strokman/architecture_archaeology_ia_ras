from measurement.models import Petrography
from measurement.forms import SubmitPetrographyForm
from core.view_mixins import UpdateMeasurementMixin


class UpdatePetrographyView(UpdateMeasurementMixin):
    model = Petrography
    form_class = SubmitPetrographyForm
