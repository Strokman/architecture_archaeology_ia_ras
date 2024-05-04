from artwork.models import Frescoe
from core.view_mixins import DeleteViewMixin


class DeleteFrescoeView(DeleteViewMixin):
    model = Frescoe