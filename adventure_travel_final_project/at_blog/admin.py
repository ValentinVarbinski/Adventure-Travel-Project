from django.contrib import admin
from django.contrib.admin import ModelAdmin

from adventure_travel_final_project.at_blog.models import AdventureTravelPost, AdventureTravelPostAuthor


@admin.register(AdventureTravelPost)
class PostAdmin(ModelAdmin):
    list_display = ('author', 'title', 'created_on')
    readonly_fields = ('created_on',)


@admin.register(AdventureTravelPostAuthor)
class PostAuthorAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name')
