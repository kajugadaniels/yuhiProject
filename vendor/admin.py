from django.contrib import admin
from vendor.models import *

class VendorAdmin(admin.ModelAdmin):
    list_display = ['store_name', 'phone_number', 'tin_number']

admin.site.register(Vendor, VendorAdmin)