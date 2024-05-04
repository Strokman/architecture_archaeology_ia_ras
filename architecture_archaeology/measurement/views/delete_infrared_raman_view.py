from measurement.models import InfraredRamanMicroscopy
from core.view_mixins import DeleteViewMixin


class DeleteInfraredRamanView(DeleteViewMixin):
    model = InfraredRamanMicroscopy