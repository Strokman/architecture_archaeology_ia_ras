from django.db import models


class IndexTable(models.Model):
  
    frescoe_id = models.IntegerField()
    artefact_id = models.IntegerField()
    indoor_artwork_id = models.IntegerField()