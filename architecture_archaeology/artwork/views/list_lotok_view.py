from artwork.models import Lotok
from core.view_mixins import ListViewMixin
from artwork.filters import LotokFilter


class ListLotokView(ListViewMixin):
    filterset_class = LotokFilter
    model = Lotok
