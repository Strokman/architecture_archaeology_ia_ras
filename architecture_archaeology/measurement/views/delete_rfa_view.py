from measurement.models import RFA
from core.view_mixins import DeleteViewMixin


class DeleteRfaView(DeleteViewMixin):
    model = RFA