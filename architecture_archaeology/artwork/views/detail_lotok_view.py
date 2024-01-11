from artwork.models import Lotok
from core.view_mixins import DetailViewMixin


class DetailLotokView(DetailViewMixin):
    model = Lotok
