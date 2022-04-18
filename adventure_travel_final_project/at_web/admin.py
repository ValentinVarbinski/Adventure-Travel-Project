from django.contrib import admin
from django.contrib.admin import ModelAdmin

from adventure_travel_final_project.at_web.models import AdventureTravelContactForm


@admin.register(AdventureTravelContactForm)
class ContactFormAdmin(ModelAdmin):
    list_display = ('subject', 'email', 'date_received', 'replied', )
    ordering = ('replied', 'date_received')
    readonly_fields = ('date_received',)