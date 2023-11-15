from django.db import models
from core.description_model import DescriptionModel


# Create your models here.
class Preservation(DescriptionModel):
    pass


class Colors(DescriptionModel):
    code = models.CharField(max_length=6, verbose_name='16-ный код')
    pass