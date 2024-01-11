from measurement.models import Roentgen
from core.view_mixins import ListViewMixin


class ListRoentgenView(ListViewMixin):
    model = Roentgen