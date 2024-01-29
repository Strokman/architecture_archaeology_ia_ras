from measurement.models import GasChromatographyMassSpectrometry
from measurement.filters import MeasurementBaseFilter


class GCMSFilter(MeasurementBaseFilter):

    class Meta:
        model = GasChromatographyMassSpectrometry
        fields = ['pigment']
