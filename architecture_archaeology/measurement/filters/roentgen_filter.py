from measurement.models import Roentgen
from measurement.filters import MeasurementBaseFilter
from helpers.models import Mineral
import django_filters
from django import forms


class RoentgenFilter(MeasurementBaseFilter):

    mineral = django_filters.ModelMultipleChoiceFilter(
        queryset=Mineral.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10})
        )
    
    class Meta:
        model = Roentgen
        fields = ()