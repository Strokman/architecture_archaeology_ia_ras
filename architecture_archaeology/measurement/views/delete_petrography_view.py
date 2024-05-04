from measurement.models import Petrography
from core.view_mixins import DeleteViewMixin


class DeletePetrographyView(DeleteViewMixin):
    model = Petrography