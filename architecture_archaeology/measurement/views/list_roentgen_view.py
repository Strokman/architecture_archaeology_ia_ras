from measurement.models import Roentgen
from core.view_mixins import ListViewMixin
from measurement.filters import RoentgenFilter


class ListRoentgenView(ListViewMixin):
    filterset_class = RoentgenFilter
    model = Roentgen