from core.view_mixins import UpdateViewMixin
from artwork.models import Lotok
from artwork.forms import SubmitLotokForm


class UpdateLotokView(UpdateViewMixin):

    model = Lotok
    form_class = SubmitLotokForm
