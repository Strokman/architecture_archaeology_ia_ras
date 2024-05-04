from building.models import Building
from core.view_mixins import DeleteViewMixin


class DeleteBuildingView(DeleteViewMixin):
    model = Building
