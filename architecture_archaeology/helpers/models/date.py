from django.db import models
from core.base_model import BaseModel


class Date(BaseModel):
    year = models.IntegerField()
    year_min = models.IntegerField()
    year_max = models.IntegerField()
