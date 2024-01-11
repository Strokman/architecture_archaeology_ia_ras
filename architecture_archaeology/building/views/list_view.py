from building.models import Building
from core.view_mixins import ListViewMixin


class BuildingListView(ListViewMixin):

    model = Building
