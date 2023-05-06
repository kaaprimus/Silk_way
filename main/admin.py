from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(PhotosNews)
admin.site.register(GalleryNews)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Date_added')

@admin.register(Ratind)
class RatindAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Date_added')