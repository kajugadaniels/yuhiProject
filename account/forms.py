from django.contrib import admin
from account.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_vendor']

admin.site.register(User, UserAdmin)