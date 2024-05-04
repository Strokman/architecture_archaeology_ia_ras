from measurement.models import GasChromatographyMassSpectrometry
from core.view_mixins import DeleteViewMixin


class DeleteGCMSView(DeleteViewMixin):
    model = GasChromatographyMassSpectrometry