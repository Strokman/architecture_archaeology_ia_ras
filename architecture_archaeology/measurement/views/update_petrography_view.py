from measurement.models import Petrography
from measurement.forms import SubmitPetrographyForm
from core.view_mixins import UpdateViewMixin


class UpdatePetrographyView(UpdateViewMixin):
    model = Petrography
    form_class = SubmitPetrographyForm
