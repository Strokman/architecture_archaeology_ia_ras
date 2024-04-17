from measurement.models import ScanningElectronMicroscopy
from measurement.forms import SubmitScanningMicroscopyForm
from core.view_mixins import UpdateMeasurementMixin


class UpdateScanningMicroscopyView(UpdateMeasurementMixin):
    model = ScanningElectronMicroscopy
    form_class = SubmitScanningMicroscopyForm
