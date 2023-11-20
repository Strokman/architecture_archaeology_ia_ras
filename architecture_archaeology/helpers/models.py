
from django.db import models
from core.description_model import DescriptionModel
from core.timestamp_model import TimestampModel
from core.base_model import BaseModel


# Create your models here.
class Preservation(DescriptionModel):
    pass


class Colors(DescriptionModel):
    code = models.CharField(max_length=7, verbose_name='16-ный код')

    def __str__(self):
        return f'{self.code}: {self.description}'


class Comment(BaseModel):
    text = models.TextField()

    def __str__(self):
        return self.text
    
class Date(BaseModel):
    year = models.IntegerField()
    year_min = models.IntegerField()
    year_max = models.IntegerField()