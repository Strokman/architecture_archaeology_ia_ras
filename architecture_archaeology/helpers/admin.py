from django.contrib import admin
from .models import Preservation, Comment, Color, Date
# Register your models here.


admin.site.register(Preservation)
admin.site.register(Color)
admin.site.register(Comment)
admin.site.register(Date)
