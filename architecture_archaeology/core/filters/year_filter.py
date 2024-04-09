# TODO: сделать макс не 2024, а сейчас из datetime

class RangeDatesFilterBase:

    def filter_dating(self, queryset, name, value):
        filter_period = {}
        filter_period['start'] = int(value.start) if value.start is not None else -10000
        filter_period['end'] = int(value.stop) if value.stop is not None else 2024
        return queryset.filter(year_min__lt=filter_period['end'],
                               year_max__gt=filter_period['start']) | \
               queryset.filter(year_min=filter_period['end'],
                               year_max=filter_period['start'])
