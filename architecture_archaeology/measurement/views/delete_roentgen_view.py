from measurement.models import Roentgen
from core.view_mixins import DeleteViewMixin


class DeleteRoentgenView(DeleteViewMixin):
    model = Roentgen