from artwork.models import Frescoe
from core.view_mixins import ListViewMixin
from artwork.filters.frescoe_filter import FrescoeFilter


class ListFrescoeView(ListViewMixin):
    filterset_class = FrescoeFilter

    model = Frescoe
