from measurement.models import RFA
from core.view_mixins import ListViewMixin


class ListRFAView(ListViewMixin):
    model = RFA