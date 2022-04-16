from django.urls import path
import adventure_travel_final_project.common.signals
from adventure_travel_final_project.at_auth.views.auth import UserRegisterView, UserLoginView, UserLogoutView, \
    UserRequireLoginView
from adventure_travel_final_project.at_auth.views.email_verification import VerifyEmailRegisterView, \
    verify_email_login_view, activate_email_view, validation_error_view
from adventure_travel_final_project.at_auth.views.password_management import UserPasswordResetView, \
    UserPasswordResetDoneView, UserPasswordResetConfirmView, UserPasswordCompleteView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('login_required/', UserRequireLoginView.as_view(), name='require login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('verify_email_register/', VerifyEmailRegisterView.as_view(), name='verify email initial'),
    path('verify_email_login/<int:pk>', verify_email_login_view, name='verify email additional'),
    path('activate_email/<int:pk>/<token>/', activate_email_view, name='activate email'),
    path('activate_email/validation_error', validation_error_view, name='validation error'),

    path('reset_password/', UserPasswordResetView.as_view(), name='reset password'),
    path('reset_password/sent/', UserPasswordResetDoneView.as_view(), name='reset password sent'),
    path('reset_password/confirm/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', UserPasswordCompleteView.as_view(), name='reset password complete'),
]
