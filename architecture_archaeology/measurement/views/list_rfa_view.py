from measurement.models import RFA
from core.view_mixins import ListViewMixin
from measurement.filters import RFAFilter


class ListRFAView(ListViewMixin):
    filterset_class = RFAFilter
    model = RFA