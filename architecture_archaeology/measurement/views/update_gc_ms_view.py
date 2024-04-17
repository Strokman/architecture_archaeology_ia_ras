from measurement.models import GasChromatographyMassSpectrometry
from measurement.forms import SubmitGCMSForm
from core.view_mixins import UpdateMeasurementMixin


class UpdateGCMSView(UpdateMeasurementMixin):
    model = GasChromatographyMassSpectrometry
    form_class = SubmitGCMSForm
