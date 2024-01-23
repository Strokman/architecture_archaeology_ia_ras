from building.models import Building
from building.filter import BuildingFilter
from core.view_mixins import ListViewMixin


class BuildingListView(ListViewMixin):
    filterset_class = BuildingFilter
    model = Building
