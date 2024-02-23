from django.db import models
from core.models.base_model import BaseModel


class YearMixin(BaseModel):

    year_min = models.IntegerField(null=True, blank=True, verbose_name='Датировка от:')
    year_max = models.IntegerField(null=True, blank=True, verbose_name='до:', help_text='Даты до н.э. должны быть отрицательными')

    def dating(self):
        a = ('г. до н.э.', 'г. н.э.')
        year_min = ''
        year_max = ''
        date = ''
        if self.year_min:
            year_min = f'{abs(self.year_min)} {a[self.year_min > 0]}'
        if self.year_max:
            year_max = f'{abs(self.year_max)} {a[self.year_max > 0]}'
        if self.year_min and self.year_max:
            date = f'{year_min} - {year_max}'
        elif self.year_min:
            date = f'Не ранее {year_min}'
        elif self.year_max:
            date = f'Не позднее {year_min}'
        for i in a:
            if date.count(i) > 1:
                date = date.replace(i, '', 1)
                date = date.replace(i, f'г{i}')
        return date

    class Meta:

        abstract = True