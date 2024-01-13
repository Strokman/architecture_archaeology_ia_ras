from measurement.models import GasChromatographyMassSpectrometry
from measurement.forms import SubmitGCMSForm

from core.view_mixins import CreateViewMixin


class SubmitGCMSView(CreateViewMixin):
    model = GasChromatographyMassSpectrometry
    form_class = SubmitGCMSForm