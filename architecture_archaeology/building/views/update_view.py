from building.forms import SubmitBuildingForm
from building.models import Building
from core.view_mixins import UpdateViewMixin


class UpdateBuildingView(UpdateViewMixin):

    model = Building
    form_class = SubmitBuildingForm
