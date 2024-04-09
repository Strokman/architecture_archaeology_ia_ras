from django import forms
import django_filters

from measurement.models import GasChromatographyMassSpectrometry
from measurement.filters import MeasurementBaseFilter
from helpers.models import Pigment


class GCMSFilter(MeasurementBaseFilter):

    pigment = django_filters.ModelMultipleChoiceFilter(
        queryset=Pigment.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10})
        )

    class Meta:
        model = GasChromatographyMassSpectrometry
        fields = ()
