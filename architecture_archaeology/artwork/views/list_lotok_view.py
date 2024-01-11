from artwork.models import Lotok
from core.view_mixins import ListViewMixin


class ListLotokView(ListViewMixin):
    model = Lotok
