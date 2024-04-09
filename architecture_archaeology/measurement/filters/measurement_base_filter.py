import django_filters

from django import forms
from django_filters import widgets
from helpers.models import Color


class MeasurementBaseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    measurement_date = django_filters.DateFromToRangeFilter(
        widget=widgets.RangeWidget(
            attrs={
                'placeholder': 'гггг-мм-дд',
                'class': 'input-group mb-3'}
                )
            )
    code = django_filters.RangeFilter(
        label='Шифр фрески/находки', method='filter_parent'
        )
    operator = django_filters.CharFilter(lookup_expr='icontains')
    equipment = django_filters.CharFilter(lookup_expr='icontains')
    conditions = django_filters.CharFilter(lookup_expr='icontains')
    comment = django_filters.CharFilter(lookup_expr='icontains')
    additional_elements = django_filters.CharFilter(lookup_expr='icontains')
    source = django_filters.CharFilter(lookup_expr='icontains')
    color = django_filters.ModelMultipleChoiceFilter(
        queryset=Color.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10})
        )

    def filter_parent(self, queryset, name, value):
        start = value.start if value.start else 1
        end = value.stop if value.stop else 10000000
        list_of_ids = [
            i.pk for i in queryset if i.parent_obj.code >= start
            and i.parent_obj.code <= end
            ]
        rv = queryset.filter(pk__in=list_of_ids)
        return rv
