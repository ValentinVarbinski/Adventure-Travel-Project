from django.urls import path

from adventure_travel_final_project.at_experiences.views import show_experiences_view, register_for_experience_view

urlpatterns = [
    path('', show_experiences_view, name='show experiences'),
    path('register/<int:pk>', register_for_experience_view, name='register for experience'),
]
