from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import SlugMixin
from core.models import TimestampMixin
from core.models import DescriptionMixin, YearMixin


class Building(DescriptionMixin, TimestampMixin, SlugMixin, YearMixin):
    class Preservation(models.TextChoices):
        PRESERVED = 'P', _('сохранился')
        DESTROYED = 'D', _('не сохранился')

    name = models.CharField(verbose_name='Название', max_length=255)
    lat = models.DecimalField(verbose_name='Широта', max_digits=23, decimal_places=20)
    long = models.DecimalField(verbose_name='Долгота', max_digits=23, decimal_places=20)
    preservation = models.CharField(verbose_name='Сохранность', null=False, max_length=100, choices=Preservation)
    comment = models.TextField(verbose_name='Примечание', null=True, blank=True)

    site = models.ForeignKey('arch_site.ArchaeologicalSite', verbose_name='Памятник', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.name}'
    
    @property
    def query_string_for_all_children(self):
        # TODO: Нужно оптимизировать, чтоб не было много запросов
        indoorartworks = self.indoorartwork_set.all()
        frescoes = self.frescoe_set.all()
        artefacts = self.artefact_set.all()
        all_children = [str(i.code) for i in indoorartworks] + [str(i.code) for i in frescoes] + [str(i.code) for i in artefacts]
        if not all_children:
            return ''
        query_string = ','.join(all_children)
        return query_string
    
    class Meta:

        verbose_name = 'Постройка'
        verbose_name_plural = 'Постройки'
        ordering = ('name', 'id')
