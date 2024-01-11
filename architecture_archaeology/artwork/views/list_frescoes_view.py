from artwork.models import Frescoe
from core.view_mixins import ListViewMixin


class ListFrescoeView(ListViewMixin):

    model = Frescoe
