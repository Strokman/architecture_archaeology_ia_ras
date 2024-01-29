from measurement.models import InfraredRamanMicroscopy
from core.view_mixins import ListViewMixin
from measurement.filters import InfraredRamanFilter


class ListInfraredRamanView(ListViewMixin):
    filterset_class = InfraredRamanFilter
    model = InfraredRamanMicroscopy