from django.db import models


class FileType(models.Model):
    name = models.CharField(max_length=255)
