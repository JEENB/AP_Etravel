from django.contrib import admin
from .models import Complaint
# Register your models here.

class AdminComplaint(admin.ModelAdmin):
    list_display        = ['name', 'email', 'status', 'note']
    list_filter         = ['status']
    readonly_fields     = ('name', 'email', 'contact', 'complaint', 'booking_code')

admin.site.register(Complaint, AdminComplaint)
