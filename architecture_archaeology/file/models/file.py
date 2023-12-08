from django.db import models
from core.timestamp_mixin import TimestampMixin


CHOICES = [
    ('F', 'фотография'),
    ('PIC', 'рисунок'),
    ('P', 'план')
    ]


class File(TimestampMixin):
    filename = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100, choices=CHOICES)
    # file_type = models.ForeignKey('helpers.FileType', on_delete=models.CASCADE)
    # bulding = models.ForeignKey('building.Building', on_delete=models.CASCADE)
