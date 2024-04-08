from measurement.models import ScanningElectronMicroscopy
from measurement.forms import SubmitScanningMicroscopyForm

from core.view_mixins import CreateMeasurementMixin


class SubmitMicroscopyView(CreateMeasurementMixin):
    model = ScanningElectronMicroscopy
    form_class = SubmitScanningMicroscopyForm
