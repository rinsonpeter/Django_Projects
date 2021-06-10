from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=('email','name','Phone','date_joined',
                    'is_admin','is_staff','is_active',
                    'profile_image','is_superuser',
                    'last_login','password')
    search_fields=('email',)
    readonly_fields=('id','date_joined','last_login')

    filter_horizontal=()
    list_filter=()
    fieldsets=()
    ordering = ('email',)

admin.site.register(Account,AccountAdmin)