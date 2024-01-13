from core.models import DescriptionMixin
from django.db import models


class Mineral(DescriptionMixin):
    formula = models.CharField(max_length=255)