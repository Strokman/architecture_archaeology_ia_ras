from measurement.models import ScanningElectronMicroscopy
from measurement.forms import SubmitScanningMicroscopyForm
from core.view_mixins import UpdateViewMixin


class UpdateScanningMicroscopyView(UpdateViewMixin):
    model = ScanningElectronMicroscopy
    form_class = SubmitScanningMicroscopyForm
