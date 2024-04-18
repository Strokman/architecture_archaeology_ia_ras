import django_filters

from django import forms
from django_filters import widgets
from helpers.models import Color


class CustomDateTimeRangeField(django_filters.filters.RangeField):

    def __init__(self, *args, **kwargs):
        fields = (
            forms.DateTimeField(input_formats=["%d.%m.%Y"]),
            forms.DateTimeField(input_formats=["%d.%m.%Y"]),
        )
        super(CustomDateTimeRangeField, self).__init__(fields, *args, **kwargs)


class CustomDateFromToRangeFilter(django_filters.RangeFilter):
    field_class = CustomDateTimeRangeField


class MeasurementBaseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    measurement_date = CustomDateFromToRangeFilter(
        widget=widgets.DateRangeWidget(
            attrs={
                'placeholder': 'дд.мм.гггг',
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
        qs = queryset.filter(pk__in=list_of_ids).order_by('pk')
        return qs
