from measurement.models import Petrography
from core.view_mixins import ListViewMixin
from measurement.filters import PetrographyFilter


class ListPetrographyView(ListViewMixin):
    filterset_class = PetrographyFilter
    model = Petrography