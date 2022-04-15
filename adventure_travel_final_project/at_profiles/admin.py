from django.contrib import admin
from django.contrib.admin import ModelAdmin

from adventure_travel_final_project.at_profiles.models import AdventureTravelProfile


@admin.register(AdventureTravelProfile)
class AdventureTravelProfileAdmin(ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'profile_picture',)
    # readonly_fields = ('user',)
    # form = UserProfileForm
