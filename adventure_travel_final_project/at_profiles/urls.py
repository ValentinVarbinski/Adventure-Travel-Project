from django.urls import path

from adventure_travel_final_project.at_profiles.views import ProfileView, edit_profile_view, ChangePasswordView, \
    MyExperiencesView, ExperienceCancelView

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('edit_profile/<int:pk>', edit_profile_view, name='edit profile'),
    path('change_password/<int:pk>', ChangePasswordView.as_view(), name='change password'),

    path('my_experiences/<username>', MyExperiencesView.as_view(), name='my experiences'),
    path('cancel/<int:pk>', ExperienceCancelView.as_view(), name='cancel experience'),

]
