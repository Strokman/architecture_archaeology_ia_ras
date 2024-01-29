from core.models import DescriptionMixin


class Material(DescriptionMixin):
    
    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'