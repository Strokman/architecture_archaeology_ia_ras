from measurement.models import RFA
from measurement.forms import SubmitRFAForm

from core.view_mixins import CreateViewMixin


class SubmitRFAView(CreateViewMixin):
    model = RFA
    form_class = SubmitRFAForm
