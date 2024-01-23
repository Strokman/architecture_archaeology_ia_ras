from measurement.models import Petrography
from measurement.forms import SubmitPetrographyForm

from core.view_mixins import CreateViewMixin


class SubmitPetrographyView(CreateViewMixin):
    model = Petrography
    form_class = SubmitPetrographyForm