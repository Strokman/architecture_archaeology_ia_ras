from measurement.models import GasChromatographyMassSpectrometry
from measurement.forms import SubmitGCMSForm

from core.view_mixins import CreateMeasurementMixin


class SubmitGCMSView(CreateMeasurementMixin):
    model = GasChromatographyMassSpectrometry
    form_class = SubmitGCMSForm
