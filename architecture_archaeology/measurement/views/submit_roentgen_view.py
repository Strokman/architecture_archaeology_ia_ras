from measurement.models import Roentgen
from measurement.forms import SubmitRoentgenForm

from core.view_mixins import CreateViewMixin


class SubmitRoentgenView(CreateViewMixin):
    model = Roentgen
    form_class = SubmitRoentgenForm