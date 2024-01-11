from measurement.models import ScanningElectronMicroscopy
from measurement.forms import SubmitMicroscopyForm

from core.view_mixins import CreateViewMixin


class SubmitMicroscopyView(CreateViewMixin):
    model = ScanningElectronMicroscopy
    form_class = SubmitMicroscopyForm
    template_name = 'form_template.html'
    success_url = '/'