from django.urls import path

from adventure_travel_final_project.at_profiles.views import ProfileView, edit_profile_view, ChangePasswordView

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('edit_profile/<int:pk>', edit_profile_view, name='edit profile'),
    path('change_password/<int:pk>', ChangePasswordView.as_view(), name='change password'),
]
