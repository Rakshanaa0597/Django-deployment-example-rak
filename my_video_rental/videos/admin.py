from django.contrib import admin
from . import models
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields=['release_year','length','title']
    list_display=['release_year','length','title']
    search_fields = ['title']
    list_filter = ['release_year']
    list_editable = ['length']
admin.site.register(models.Movie,MovieAdmin)
admin.site.register(models.Customer)