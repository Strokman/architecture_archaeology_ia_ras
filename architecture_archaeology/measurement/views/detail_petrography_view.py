from measurement.models import Petrography

from core.view_mixins import DetailViewMixin


class DetailPetrographyView(DetailViewMixin):
    model = Petrography
