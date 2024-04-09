from measurement.models import Roentgen

from core.view_mixins import DetailViewMixin


class DetailRoentgenView(DetailViewMixin):
    model = Roentgen
    template_name = 'roentgen/detail.html'
