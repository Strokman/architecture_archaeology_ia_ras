from measurement.models import Roentgen
from measurement.forms import SubmitRoentgenForm
from core.view_mixins import UpdateViewMixin


class UpdateRoentgenView(UpdateViewMixin):
    model = Roentgen
    form_class = SubmitRoentgenForm
