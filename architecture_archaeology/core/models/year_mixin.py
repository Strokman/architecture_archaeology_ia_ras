from django.db import models
from core.models.base_model import BaseModel


class YearMixin(BaseModel):

    """
    Во многих моделях используется поле Даты для объектов,
    поэтому сделал этот класс, чтоб от него отнаследоваться.
    """

    year_min = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Датировка от:'
        )
    year_max = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='до:',
        help_text='Даты до н.э. должны быть отрицательными'
        )

    def dating(self):
        """
        Функция для формирования строки датировки.
        Сделано ветвление выбора в соотв. с наличием данных.
        Год может быть только стартовый, или конечный, или и то,
        и другое. В соотв. с этим формируется строка.
        Так было указано в ТЗ.
        """
        eras = ('г. до н.э.', 'г.')
        year_min = ''
        year_max = ''
        date = ''
        if self.year_min:
            year_min = f'{abs(self.year_min)} {eras[self.year_min > 0]}'
        if self.year_max:
            year_max = f'{abs(self.year_max)} {eras[self.year_max > 0]}'
        if self.year_min and self.year_max:
            date = f'{year_min} - {year_max}'
        elif self.year_min:
            date = f'Не ранее {year_min}'
        elif self.year_max:
            date = f'Не позднее {year_max}'
        if (self.year_min and self.year_min > 0) and (self.year_max and self.year_max > 0):
            date = date.replace('г.', '', 1)
            date = date.replace('г.', 'гг.')
        elif (self.year_min and self.year_min < 0) and (self.year_max and self.year_max < 0):
            date = date.replace('г. до н.э.', '', 1)
            date = date.replace('г.', 'гг.')
        return date

    class Meta:

        abstract = True