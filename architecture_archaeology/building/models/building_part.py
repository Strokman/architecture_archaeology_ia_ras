from django.db import models
# from core import DescriptionMixin


class BuildingPart(models.Model):
    
    name = models.CharField(verbose_name='Название', max_length=255)

    # building = models.ForeignKey('building.Building', on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Элемент постройки'
        verbose_name_plural = 'Элементы постройки'
