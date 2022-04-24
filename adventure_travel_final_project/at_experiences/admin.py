from django.contrib import admin
from django.contrib.admin import ModelAdmin

from adventure_travel_final_project.at_experiences.models import AdventureTravelExperience, AdventureTravelRegistration


@admin.register(AdventureTravelExperience)
class ExperiencesAdmin(ModelAdmin):
    list_display = ('title', 'category', 'date', 'price', 'spots')
    ordering = ('date',)


@admin.register(AdventureTravelRegistration)
class RegistrationLogAdmin(ModelAdmin):
    list_display = ('experience', 'client', 'registration_date',)
    fieldsets = (
        (None, {'fields': ('experience', 'client', 'registration_date')}),
    )
    readonly_fields = ('registration_date',)
