from measurement.models import RFA
from measurement.filters import MeasurementBaseFilter
import django_filters


class RFAFilter(MeasurementBaseFilter):

    elements = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = RFA
        fields = []