from measurement.models import RFA

from core.view_mixins import DetailViewMixin


class DetailRFAView(DetailViewMixin):
    model = RFA
