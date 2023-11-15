from django.contrib import admin
from .models import Preservation, Comment, Colors
# Register your models here.


admin.site.register(Preservation)
admin.site.register(Colors)
admin.site.register(Comment)