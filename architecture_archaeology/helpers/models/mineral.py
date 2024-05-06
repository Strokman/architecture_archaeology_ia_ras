from core.models import DescriptionMixin
from django.db import models


class Mineral(DescriptionMixin):
    formula = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Минерал'
        verbose_name_plural = 'Минералы'
        ordering = ('description', 'id')