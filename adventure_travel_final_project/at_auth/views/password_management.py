from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from adventure_travel_final_project.at_auth.forms.password_reset import UserPasswordResetForm, UserSetNewPasswordForm


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'auth/password_management/reset_password.html'
    from_email = 'adventure.travel.app.team@gmail.com'
    form_class = UserPasswordResetForm
    success_url = reverse_lazy('reset password sent')


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'auth/password_management/reset_password_sent.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'auth/password_management/reset_password_confirm.html'
    form_class = UserSetNewPasswordForm
    success_url = reverse_lazy('reset password complete')


class UserPasswordCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'auth/password_management/reset_password_complete.html'
