from core.view_mixins import UpdateViewMixin
from artwork.models import Frescoe
from artwork.forms import SubmitFrescoeForm


class UpdateFrescoeView(UpdateViewMixin):

    model = Frescoe
    form_class = SubmitFrescoeForm