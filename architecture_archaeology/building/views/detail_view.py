from building.models import Building
from core.view_mixins import DetailViewMixin


class BuildingDetailView(DetailViewMixin):

    model = Building
