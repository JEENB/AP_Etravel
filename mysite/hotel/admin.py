from django.contrib import admin
from .models import Hotel, Category, Images, Review, Booking, BookingInfo
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


class AdminBookingInfo(admin.ModelAdmin):
    list_display        = ['user', 'hotel', 'guest', 'check_in', 'check_out', 'total']
    list_filter         = ['hotel', 'user', 'check_in']
    readonly_fields     = ('user', 'hotel', 'first_name', 'last_name', 'contact', 'address', 'email', 'guest','guest_name',  'check_in', 'check_out', 'total', 'cname', 'ccnum','expmonth','expyear','cvv', 'bookingcode')


admin.site.register(Category, AdminCategory)
admin.site.register(Hotel, AdminHotel)
admin.site.register(Images)
admin.site.register(BookingInfo, AdminBookingInfo)

admin.site.register(Review, AdminReview)

