from measurement.models import ScanningElectronMicroscopy
from measurement.forms import SubmitScanningMicroscopyForm

from core.view_mixins import CreateViewMixin


class SubmitMicroscopyView(CreateViewMixin):
    model = ScanningElectronMicroscopy
    form_class = SubmitScanningMicroscopyForm
