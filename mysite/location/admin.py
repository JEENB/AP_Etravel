from django.contrib import admin
from .models import Locations, Images
# Register your models here.

class AdminImages(admin.TabularInline):
    model        = Images
    extra        = 3

class AdminLocations(admin.ModelAdmin):
    list_display        = ['country','location','image_tag' ]
    list_filter         = ['country']
    inlines             = [AdminImages]

admin.site.register(Locations, AdminLocations)
admin.site.register(Images)