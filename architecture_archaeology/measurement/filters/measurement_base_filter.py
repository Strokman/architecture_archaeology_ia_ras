import django_filters
from django_filters import widgets
from helpers.models import Color


class MeasurementBaseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    measurement_date = django_filters.DateFromToRangeFilter(widget=widgets.RangeWidget(attrs={'placeholder': 'гггг-мм-дд', 'class': 'input-group mb-3'}))
    operator = django_filters.CharFilter(lookup_expr='icontains')
    equipment = django_filters.CharFilter(lookup_expr='icontains')
    conditions = django_filters.CharFilter(lookup_expr='icontains')
    comment = django_filters.CharFilter(lookup_expr='icontains')
    additional_elements = django_filters.CharFilter(lookup_expr='icontains')
    source = django_filters.CharFilter(lookup_expr='icontains')
    color = django_filters.ModelMultipleChoiceFilter(queryset=Color.objects.all())
