from django.contrib import admin
from .models import Hotel, Category, Images, Review, Booking
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

class AdminReview(admin.ModelAdmin):
    list_display        = ['comment', 'rate', 'user','created', 'hotel_name' ]
    list_filter         = ['hotel', 'user']


class AdminBooking(admin.ModelAdmin):
    list_display        = ['user', 'hotel', 'guest', 'check_in', 'check_out', 'amount']
    list_filter         = ['hotel', 'user', 'check_in']
    readonly_fields     = ('user', 'hotel', 'guest', 'check_in', 'check_out')


admin.site.register(Category, AdminCategory)
admin.site.register(Hotel, AdminHotel)
admin.site.register(Images)
admin.site.register(Review, AdminReview)
admin.site.register(Booking, AdminBooking)

