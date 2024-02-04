from building.models import Building
from core.view_mixins import DetailViewMixin


class BuildingDetailView(DetailViewMixin):
    template_name = 'detail_arch_object.html'
    model = Building
