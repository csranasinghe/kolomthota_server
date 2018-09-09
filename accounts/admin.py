from django.contrib import admin
from .models import Account, ShippingAgent
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = Account
    list_filter = ['user_type']
    list_display = ['get_full_name']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'classes': ('wide',), 'fields': ('first_name', 'last_name', 'email', 'user_type')}),
     )


admin.site.register(Account, CustomUserAdmin)
admin.site.register(ShippingAgent)

