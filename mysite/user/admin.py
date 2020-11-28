from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','address', 'contact', 'city', 'pincode', 'country']
    list_filter  = ['city', 'pincode', 'country']


admin.site.register(Profile, ProfileAdmin)