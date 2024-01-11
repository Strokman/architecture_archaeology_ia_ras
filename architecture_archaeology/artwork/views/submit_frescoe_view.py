from artwork.models import Frescoe
from artwork.forms import SubmitFrescoeForm

from core.view_mixins import CreateViewMixin


class SubmitFrescoeView(CreateViewMixin):
    model = Frescoe
    form_class = SubmitFrescoeForm
