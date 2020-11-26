from django.contrib import admin
from .models import Hotel, Category, Images
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display        = ['country']
    

class AdminImages(admin.TabularInline):
    model        = Images
    extra        = 3

class AdminHotel(admin.ModelAdmin):
    list_display        = ['title', 'price','country','location','image_tag' ]
    list_filter         = ['country', 'location']
    prepopulated_fields = {"slug": ("title",)}
    inlines             = [AdminImages]

admin.site.register(Category, AdminCategory)
admin.site.register(Hotel, AdminHotel)
admin.site.register(Images)