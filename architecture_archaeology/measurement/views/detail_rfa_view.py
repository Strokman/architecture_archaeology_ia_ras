from measurement.models import RFA

from core.view_mixins import DetailViewMixin


class DetailRFAView(DetailViewMixin):
    model = RFA
    template_name = 'microscopy_rfa/detail.html'
