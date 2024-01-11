from measurement.models import GasChromatographyMassSpectrometry
from measurement.forms import SubmitGCMSForm
from core.view_mixins import UpdateViewMixin


class UpdateGCMSView(UpdateViewMixin):
    model = GasChromatographyMassSpectrometry
    form_class = SubmitGCMSForm