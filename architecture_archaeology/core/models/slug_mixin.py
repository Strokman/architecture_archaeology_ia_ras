from core.utils import slugify
from django.db import models
from core.models.base_model import BaseModel
from uuid import uuid1, uuid4


class SlugMixin(BaseModel):

    slug = models.SlugField(max_length=500, unique=True, null=False, db_index=True)

    creator = models.ForeignKey('auth.User', null=True, related_name='creator+', on_delete=models.PROTECT)
    editor = models.ForeignKey('auth.User', null=True, related_name='editor+', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if hasattr(self, 'name') and self.name:
            self.slug = slugify(self.name, allow_unicode=True) + '-' + str(uuid1())
        else:
            self.slug = str(uuid4())
        super().save(*args, **kwargs)

    class Meta:

        abstract = True
