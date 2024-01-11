from artwork.models import Frescoe
from core.view_mixins import DetailViewMixin


class DetailFrescoeView(DetailViewMixin):
    model = Frescoe
