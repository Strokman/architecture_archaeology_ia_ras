from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import SlugMixin, TimestampMixin


class Petrography(SlugMixin, TimestampMixin):

    class Pores(models.TextChoices):
        NO_PORES = 'N', _('Пор нет')
        SM = 'SM', _('Поры мелкие')
        LG = 'LG', _('Поры крупные')

    measurement_date = models.DateField(verbose_name='Дата исследования', null=False)
    number = models.CharField(verbose_name='Номер шлифа', null=False, max_length=255)

    operator = models.CharField(verbose_name='Оператор', max_length=255, null=False)
    equipment = models.CharField(verbose_name='Оборудование', max_length=255, null=False)
    binder_name = models.CharField(verbose_name='Вяжущее название', max_length=255, null=True, blank=True)
    binder_percent = models.IntegerField(verbose_name='Вяжущее %', null=True, blank=True)
    binder_description = models.TextField(verbose_name='Вяжущее описание', null=True, blank=True)

    filler_percent = models.IntegerField(verbose_name='Заполнитель %', null=True, blank=True)
    filler_contains = models.ManyToManyField('helpers.Filler', blank=True, verbose_name='Заполнитель состав')
    filler_description = models.TextField(verbose_name='Заполнитель описание', null=True, blank=True)
    color = models.ManyToManyField('helpers.Color', blank=True, verbose_name='Цвета')

    pores = models.CharField(verbose_name='Наличие пор', max_length=100, null=True, blank=True, choices=Pores)
    pores_diameter = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Диаметр пор', null=True, blank=True)
    comment = models.TextField(verbose_name='Примечание', null=True, blank=True)

    def __str__(self) -> str:
        return f'Шлиф № {self.number}'

    class Meta:
        verbose_name = verbose_name_plural = 'Петрография'
