from django.contrib import admin
from .models import Preservation, Comment, Color, Date, Country, Region
# Register your models here.


admin.site.register(Preservation)
admin.site.register(Color)
admin.site.register(Comment)
admin.site.register(Date)
admin.site.register(Country)
admin.site.register(Region)
