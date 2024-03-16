from django.contrib import admin
from store.models import *

class VendorAdmin(admin.ModelAdmin):
    list_display = ['store_name', 'phone_number', 'tin_number']

    admin.site.register(Vendor, VendorAdmin)