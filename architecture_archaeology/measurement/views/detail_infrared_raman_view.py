from measurement.models import InfraredRamanMicroscopy

from core.view_mixins import DetailViewMixin


class DetailInfraredRamanView(DetailViewMixin):
    model = InfraredRamanMicroscopy
