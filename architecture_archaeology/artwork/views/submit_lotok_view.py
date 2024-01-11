from artwork.models import Lotok
from artwork.forms import SubmitLotokForm

from core.view_mixins import CreateViewMixin


class SubmitLotokView(CreateViewMixin):
    model = Lotok
    form_class = SubmitLotokForm
