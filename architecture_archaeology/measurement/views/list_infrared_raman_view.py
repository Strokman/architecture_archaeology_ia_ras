from measurement.models import InfraredRamanMicroscopy
from core.view_mixins import ListViewMixin


class ListInfraredRamanView(ListViewMixin):
    model = InfraredRamanMicroscopy