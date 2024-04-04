import django_filters
from django import forms
from arch_site.models import ArchaeologicalSite
from helpers.models import Region
from core.filters import RangeDatesFilterBase


class ArchSiteFilter(django_filters.FilterSet, RangeDatesFilterBase):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    comment = django_filters.CharFilter(lookup_expr='contains')
    year_min = django_filters.RangeFilter(
        label='Датировка', method='filter_dating'
        )
    region = django_filters.ModelMultipleChoiceFilter(
        queryset=Region.objects.all().order_by('-country', 'name'),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10})
        )

    class Meta:
        model = ArchaeologicalSite
        fields = []
