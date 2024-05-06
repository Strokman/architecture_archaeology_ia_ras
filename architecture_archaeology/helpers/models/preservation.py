from core.models import DescriptionMixin


# Create your models here.
class Preservation(DescriptionMixin):
        
    class Meta:
        verbose_name = verbose_name_plural = 'Сохранность'
        ordering = ('description', 'id')
