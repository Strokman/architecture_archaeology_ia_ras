from measurement.models import Petrography
from core.view_mixins import ListViewMixin


class ListPetrographyView(ListViewMixin):
    model = Petrography