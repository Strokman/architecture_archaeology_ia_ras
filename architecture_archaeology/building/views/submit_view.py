from building.forms import SubmitBuildingForm
from building.models import Building
from core.view_mixins import CreateViewMixin
# Create your views here.


class SubmitBuildingView(CreateViewMixin):

    model = Building
    form_class = SubmitBuildingForm
