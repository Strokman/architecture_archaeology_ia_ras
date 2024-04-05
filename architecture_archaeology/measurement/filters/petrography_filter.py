from measurement.models import Petrography
import django_filters
from django_filters import widgets


class PetrographyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    number = django_filters.CharFilter(lookup_expr='icontains')
    measurement_date = django_filters.DateFromToRangeFilter(widget=widgets.RangeWidget(attrs={'placeholder': 'гггг-мм-дд', 'class': 'input-group mb-3'}))
    operator = django_filters.CharFilter(lookup_expr='icontains')
    equipment = django_filters.CharFilter(lookup_expr='icontains')

    binder_name = django_filters.CharFilter(lookup_expr='icontains')
    filler_description = django_filters.CharFilter(lookup_expr='icontains')
    comment = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Petrography
        fields = ('name', 'pores')
