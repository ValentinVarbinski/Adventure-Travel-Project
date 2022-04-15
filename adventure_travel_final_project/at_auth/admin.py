from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from adventure_travel_final_project.at_auth.models import AdventureTravelUser


@admin.register(AdventureTravelUser)
class AdventureTravelUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email',
                           'password',
                           'is_staff',
                           'is_superuser',
                           'is_verified',
                           'is_active',
                           'date_joined',
                           )}),
        ('Permissions', {
            'fields': ('groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined',)


