from measurement.models import RFA
from measurement.forms import SubmitRFAForm
from core.view_mixins import UpdateViewMixin


class UpdateRFAView(UpdateViewMixin):
    model = RFA
    form_class = SubmitRFAForm
