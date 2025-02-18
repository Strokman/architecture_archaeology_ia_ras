# TODO: сделать макс не 2024, а текущий год из datetime

class RangeDatesFilterBase:
    """
    Класс написан для реализации метода фильтрации по датам:
    может быть обе даты - начало и конец интервала,
    а может быть только начало ("не раньше, чем") или
    только конец интервала ("не позже чем").
    На данный момент я ограничил интервалы не раньше чем -10000 до н.э.
    Так как архитектурных памятников старше очень мало во всем мире.
    По необходимости можно сделать этот интервал больше
    """

    def filter_dating(self, queryset, name, value):
        """
        В зависимости от ввода пользователя формируется словарь,
        где содержится начало и конеч интервала поиска.
        В целом реализовано как сопоставление двух векторов.
        """
        filter_period = {}
        filter_period['start'] = int(value.start) if value.start is not None else -10000
        filter_period['end'] = int(value.stop) if value.stop is not None else 2024
        return queryset.filter(year_min__lt=filter_period['end'],
                               year_max__gt=filter_period['start']) | \
               queryset.filter(year_min=filter_period['end'],
                               year_max=filter_period['start'])
